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
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def load_pipeline(
    path: str,
    *,
    level: str | None = None,
    limit: int | None = None,
    chunk_size: int = 2,
    encoding: str = "utf-8",
) -> Iterator[tuple[LogRecord, ...]]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def summarize_levels(source: LineSource, *, limit: int | None = None) -> dict[str, int]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
