from __future__ import annotations

from typing import Generic, TypeVar

V = TypeVar("V")


class DirectedMixin(Generic[V]):
    """Mixin for directed graphs.

This mixin is intentionally thin: it exists to participate in the cooperative
`add_edge` chain and to make MRO visible.
"""

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


class UndirectedMixin(Generic[V]):
    """Mixin for undirected graphs (adds edges in both directions)."""

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


class WeightedMixin(Generic[V]):
    """Mixin that requires an explicit non-negative weight."""

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


class UnweightedMixin(Generic[V]):
    """Mixin that forbids explicit weights and forces weight=1."""

    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError
