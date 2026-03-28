from __future__ import annotations

from typing import Dict, Generic, Iterator, List, TypeVar

from .base import Edge

V = TypeVar("V")


class Graph(Generic[V]):
    """Graph implementation via composition.

This class provides the same *observable behavior* as the mixin-based variants,
but without multiple inheritance.
"""

    def __init__(self, *, directed: bool, weighted: bool) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

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

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def neighbors(self, u: V) -> List[V]:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def iter_edges(self, u: V) -> Iterator[Edge[V]]:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError
