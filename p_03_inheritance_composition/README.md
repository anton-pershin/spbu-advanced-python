# Practicum 3: Inheritance and Composition (Graphs + BFS/Dijkstra)

This practicum is about using classes to model *variants* of the same data structure
and then comparing two design techniques:

- inheritance (including cooperative multiple inheritance via `super()` and MRO)
- composition (policies/strategies injected into a single class)

We work with a classic algorithms topic: **graphs** and shortest paths.

## Prerequisites

You are expected to know:

- how to define classes and methods
- what an instance attribute is
- basic containers (`dict`, `list`, `set`, `deque`)

You are *not* expected to know inheritance yet.

## Background: inheritance

Inheritance lets you create a new class based on an existing one.

```python
class A:
    def f(self) -> str:
        return "A"

class B(A):
    pass

b = B()
assert b.f() == "A"  # B inherits method f from A
```

### Overriding

A subclass can redefine a method (override it):

```python
class B(A):
    def f(self) -> str:
        return "B"

assert B().f() == "B"

### Overriding with a different argument list

In Python, methods are looked up **by name only**. There is no "overloading" by
signature like in some other languages. If a subclass defines a method with the
same name but a *different set of parameters*, it still overrides the base
method.

What happens then depends on how you call it:

```python
class A:
    def f(self, x: int) -> int:
        return x + 1

class B(A):
    def f(self, x: int, y: int) -> int:  # different signature
        return x + y

b = B()

b.f(1, 2)  # OK -> 3
b.f(1)     # TypeError: missing required argument 'y'
```

This is a common source of bugs in inheritance-heavy designs: code written
against the base class expects `f(x)`, but a subclass silently changed the
callable interface.

Practical rule: when overriding, keep the method signature compatible.
If you need flexibility, use defaults and/or `*args, **kwargs` carefully.

In *cooperative mixins* this becomes even more important: every class in the
`super()` chain must agree on what arguments are passed along.
```

### `super()`

Often you want to *extend* a base method instead of replacing it.
`super()` calls the next implementation in the inheritance chain.

```python
class B(A):
    def f(self) -> str:
        return super().f() + "+B"

assert B().f() == "A+B"
```

## Background: multiple inheritance, MRO, and cooperative mixins

Python allows *multiple inheritance*:

```python
class C(A, B):
    ...
```

When multiple base classes define the same method name, Python must decide which
implementation runs first. The rule is called **MRO** (Method Resolution Order).

You can inspect it:

```python
print(C.mro())
```

### MRO: main rules (how the order is chosen)

Python computes MRO using an algorithm called **C3 linearization**. You do not
need to memorize the algorithm, but you should know the rules it guarantees.

For a class `class C(A, B): ...` the MRO is a single list starting with `C`.
When Python needs `obj.method`, it searches classes in that list from left to
right.

The important rules:

1) Local precedence order: bases are considered left-to-right.
   If both `A` and `B` define `f`, then in `C(A, B)` Python will pick `A.f`.

2) Parent before its parents: a class always appears before any of its own base
   classes. (A subclass beats its base.)

3) Monotonicity: the relative order of classes in a base's MRO is preserved in
   the subclass MRO. This prevents "surprising" reorderings.

The classic example is the diamond:

```python
class A:
    def f(self) -> str:
        return "A"

class B(A):
    def f(self) -> str:
        return "B->" + super().f()

class C(A):
    def f(self) -> str:
        return "C->" + super().f()

class D(B, C):
    pass

print([cls.__name__ for cls in D.mro()])
# ['D', 'B', 'C', 'A', 'object']

print(D().f())
# B->C->A
```

Note what happens:

- `D` inherits from `B` and `C` (left-to-right), so `B` comes before `C`.
- Both `B` and `C` eventually call `super().f()`. Because `super()` follows the
  MRO, you get a chain `B -> C -> A` instead of calling `A` twice.

In this practicum, mixins rely on exactly this property: each mixin contributes
its piece and then calls `super()` so the next class in the MRO can contribute.

### Mixins

A **mixin** is a small class that adds one focused behavior and is meant to be
combined with other classes.

Important: for mixins to compose, they must be **cooperative**:

- they implement the method
- they call `super().method(...)`

This creates a *chain* where every class in the MRO gets a chance to contribute.

If you forget `super()`, the chain breaks and some behavior silently disappears.

## Background: composition

**Composition** means: instead of building many subclasses, you build one class
that *contains* smaller objects (or policies) and delegates work to them.

In this practicum we will model:

- directed vs undirected insertion rules
- weighted vs unweighted weight rules

First via inheritance (mixins), then via composition (flags/policies in one class).

Composition often wins when you have many independent dimensions of variation.
For example, 2x2 variants (directed/undirected) x (weighted/unweighted) already
suggests 4 subclasses; more dimensions quickly becomes unmanageable.

## Background: abstract interfaces (ABC)

Sometimes you want to say: "any class that wants to be used here must implement
these methods".

Python's standard tool for this is `abc.ABC` (Abstract Base Class) and
`@abstractmethod`.

```python
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

V = TypeVar("V")


class GraphAPI(ABC, Generic[V]):
    @abstractmethod
    def neighbors(self, u: V) -> list[V]:
        raise NotImplementedError

    @abstractmethod
    def iter_edges(self, u: V) -> Iterable[object]:
        raise NotImplementedError
```

What this gives you:

- you can inherit from `GraphAPI` to document the contract
- if a subclass forgets to implement an abstract method, Python will refuse to
  instantiate it (you'll get a `TypeError` at runtime)

In this practicum we use a small informal interface ("duck typing") in the
algorithms, but the same idea can be expressed with an ABC. We will return to
ABCs in more detail later in the course.

## Learning goals

By the end you should be able to:

- implement a small graph data structure (adjacency map)
- implement BFS shortest path (unweighted graphs)
- implement Dijkstra shortest path (non-negative weights)
- implement graph variants via *cooperative mixins* and understand why `super()` matters
- refactor the same feature set to composition (directedness + weight rules)

## How to run

Run everything from the repo root.

Template checks:

```bash
python -m p_03_inheritance_composition.template.check
```

Reference solution checks:

```bash
python -m p_03_inheritance_composition.solution.check
```

## What you implement

Your work is in `p_03_inheritance_composition/template/graphs/`.

You must implement:

1) Core storage and interface (`GraphBase`)
2) Mixins for directed/undirected and weighted/unweighted behavior
3) Algorithms `bfs_shortest_path` and `dijkstra_shortest_path`
4) A composition-based `Graph` with the same observable behavior as mixin variants

The checks intentionally use only the public API exported from
`p_03_inheritance_composition.template.graphs`.

## How the mixin design is supposed to work (important)

The core class `GraphBase` stores edges and defines the *bottom* implementation
of `add_edge`: it adds exactly one directed arc `u -> v`.

Then mixins implement policies:

- `UndirectedMixin`: turns one `add_edge(u, v)` into two arcs (`u -> v` and `v -> u`)
- `DirectedMixin`: mostly exists to make the MRO explicit (still must call `super()`)
- `WeightedMixin`: requires explicit non-negative `weight`
- `UnweightedMixin`: forbids explicit `weight` and forces weight = 1

All of them must call `super().add_edge(...)` so they can be combined.

The checks include a case where mixin order is swapped:

- `class A(UnweightedMixin, UndirectedMixin, GraphBase)`
- `class B(UndirectedMixin, UnweightedMixin, GraphBase)`

Both must work.

Hint: if you are confused about what happens, print the MRO:

```python
print(A.mro())
print(B.mro())
```

## Algorithms

You implement two shortest-path algorithms that work through a tiny interface:

- `neighbors(u)` for BFS
- `iter_edges(u)` (edges contain `to` and `weight`) for Dijkstra

The goal is that the *same* `bfs_shortest_path` / `dijkstra_shortest_path` code
works on both implementations:

- mixin-based graph variants
- composition-based `Graph(directed=..., weighted=...)`

In this practicum, mixins *must* call `super()`.

The checks include a case where mixin order is swapped:

- `class A(UnweightedMixin, UndirectedMixin, GraphBase)`
- `class B(UndirectedMixin, UnweightedMixin, GraphBase)`

Both must work.
