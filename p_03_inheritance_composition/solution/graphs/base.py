from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Iterator, List, TypeVar

V = TypeVar("V")


@dataclass(frozen=True)
class Edge(Generic[V]):
    to: V
    weight: float


class GraphBase(Generic[V]):
    """Adjacency-map graph storage.

Bottom of the cooperative `add_edge` chain.
"""

    def __init__(self) -> None:
        self._adj: Dict[V, Dict[V, float]] = {}

    def __contains__(self, vertex: object) -> bool:
        return vertex in self._adj

    def add_vertex(self, vertex: V) -> None:
        self._adj.setdefault(vertex, {})

    def add_edge(self, u: V, v: V, weight: float | None = 1.0) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        if weight is None:
            raise ValueError("weight is required by the current policy")
        self._adj[u][v] = float(weight)

    def neighbors(self, u: V) -> List[V]:
        if u not in self._adj:
            raise KeyError(u)
        return list(self._adj[u].keys())

    def iter_edges(self, u: V) -> Iterator[Edge[V]]:
        if u not in self._adj:
            raise KeyError(u)
        for v, w in self._adj[u].items():
            yield Edge(to=v, weight=w)

    def vertices(self) -> Iterable[V]:
        return self._adj.keys()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(n={len(self._adj)})"
