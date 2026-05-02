from __future__ import annotations

from collections import Counter
from itertools import islice
from typing import Iterable, Iterator, Sequence, TypeVar

from .protocols import BatchConsumer
from .transforms import LogRecord

T = TypeVar("T")


def chunked(items: Iterable[T], size: int) -> Iterator[tuple[T, ...]]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def count_by_level(records: Iterable[LogRecord]) -> dict[str, int]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def consume_batches(batches: Iterable[Sequence[T]], consumer: BatchConsumer[T]) -> int:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
