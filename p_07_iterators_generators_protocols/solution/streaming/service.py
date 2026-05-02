from __future__ import annotations

from typing import Iterator

from .batching import chunked, count_by_level
from .protocols import LineSource
from .sources import read_lines
from .transforms import LogRecord, filter_by_level, parse_records, take


def build_pipeline(
    source: LineSource,
    *,
    level: str | None = None,
    limit: int | None = None,
    chunk_size: int = 2,
) -> Iterator[tuple[LogRecord, ...]]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    records = parse_records(source)
    if level is not None:
        records = filter_by_level(records, level)
    if limit is not None:
        records = take(records, limit)
    return chunked(records, chunk_size)


def load_pipeline(
    path: str,
    *,
    level: str | None = None,
    limit: int | None = None,
    chunk_size: int = 2,
    encoding: str = "utf-8",
) -> Iterator[tuple[LogRecord, ...]]:
    return build_pipeline(
        read_lines(path, encoding=encoding),
        level=level,
        limit=limit,
        chunk_size=chunk_size,
    )


def summarize_levels(source: LineSource, *, limit: int | None = None) -> dict[str, int]:
    records = parse_records(source)
    if limit is not None:
        records = take(records, limit)
    return count_by_level(records)
