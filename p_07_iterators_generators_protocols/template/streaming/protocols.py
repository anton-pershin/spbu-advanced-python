from __future__ import annotations

from typing import Iterator, Protocol, Sequence, TypeVar, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class LineSource(Protocol):
    def __iter__(self) -> Iterator[str]:
        ...


@runtime_checkable
class BatchConsumer(Protocol[T]):
    def consume(self, batch: Sequence[T]) -> None:
        ...
