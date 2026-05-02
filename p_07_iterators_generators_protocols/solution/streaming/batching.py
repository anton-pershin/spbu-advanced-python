from __future__ import annotations

from collections import Counter
from itertools import islice
from typing import Iterable, Iterator, Sequence, TypeVar

from .protocols import BatchConsumer
from .transforms import LogRecord

T = TypeVar("T")


def chunked(items: Iterable[T], size: int) -> Iterator[tuple[T, ...]]:
    if size <= 0:
        raise ValueError("size must be positive")

    iterator = iter(items)
    while True:
        batch = tuple(islice(iterator, size))
        if not batch:
            break
        yield batch


def count_by_level(records: Iterable[LogRecord]) -> dict[str, int]:
    counts = Counter(record.level for record in records)
    return dict(sorted(counts.items()))


def consume_batches(batches: Iterable[Sequence[T]], consumer: BatchConsumer[T]) -> int:
    count = 0
    for batch in batches:
        consumer.consume(batch)
        count += 1
    return count
