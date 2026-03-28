from __future__ import annotations

from typing import Generic, TypeVar

V = TypeVar("V")


class DirectedMixin(Generic[V]):
    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        # Forward to the next class in MRO.
        # Weight policy (weighted/unweighted) is implemented by other mixins.
        super().add_edge(u, v, weight)  # type: ignore[misc]


class UndirectedMixin(Generic[V]):
    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:
        # Add edges in both directions.
        super().add_edge(u, v, weight)  # type: ignore[misc]
        super().add_edge(v, u, weight)  # type: ignore[misc]


class WeightedMixin(Generic[V]):
    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:  # type: ignore[override]
        if weight is None:
            raise ValueError("weighted graph requires weight")
        w = float(weight)
        if w < 0:
            raise ValueError("edge weight must be non-negative")
        super().add_edge(u, v, w)  # type: ignore[misc]


class UnweightedMixin(Generic[V]):
    def add_edge(self, u: V, v: V, weight: float | None = None) -> None:  # type: ignore[override]
        if weight is not None:
            raise ValueError("unweighted graph forbids explicit weight")
        super().add_edge(u, v, 1.0)  # type: ignore[misc]
