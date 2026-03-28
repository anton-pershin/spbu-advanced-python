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

This class is the bottom of the cooperative `add_edge` chain.
Mixins should override `add_edge` and call `super().add_edge(...)`.
"""

    def __init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    # Expected internal storage type:
    # self._adj: Dict[V, Dict[V, float]]
    _adj: Dict[V, Dict[V, float]]

    def __contains__(self, vertex: object) -> bool:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def add_vertex(self, vertex: V) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def add_edge(self, u: V, v: V, weight: float | None = 1.0) -> None:
        """Add exactly one directed arc (u -> v) with the given weight."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def neighbors(self, u: V) -> List[V]:
        """Return outgoing neighbors of u."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def iter_edges(self, u: V) -> Iterator[Edge[V]]:
        """Iterate outgoing edges of u."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def vertices(self) -> Iterable[V]:
        return self._adj.keys()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(n={len(self._adj)})"
