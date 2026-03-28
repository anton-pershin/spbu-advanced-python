from __future__ import annotations

from typing import Dict, Generic, Iterator, List, TypeVar

from .base import Edge

V = TypeVar("V")


class Graph(Generic[V]):
    def __init__(self, *, directed: bool, weighted: bool) -> None:
        self._directed = bool(directed)
        self._weighted = bool(weighted)
        self._adj: Dict[V, Dict[V, float]] = {}

    def __contains__(self, vertex: object) -> bool:
        return vertex in self._adj

    def add_vertex(self, vertex: V) -> None:
        self._adj.setdefault(vertex, {})

    def _add_arc(self, u: V, v: V, w: float) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u][v] = w

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        if self._weighted:
            if weight is None:
                raise ValueError("weighted graph requires weight")
            w = float(weight)
            if w < 0:
                raise ValueError("edge weight must be non-negative")
        else:
            if weight is not None:
                raise ValueError("unweighted graph forbids explicit weight")
            w = 1.0

        self._add_arc(u, v, w)
        if not self._directed:
            self._add_arc(v, u, w)

    def neighbors(self, u: V) -> List[V]:
        if u not in self._adj:
            raise KeyError(u)
        return list(self._adj[u].keys())

    def iter_edges(self, u: V) -> Iterator[Edge[V]]:
        if u not in self._adj:
            raise KeyError(u)
        for v, w in self._adj[u].items():
            yield Edge(to=v, weight=w)
