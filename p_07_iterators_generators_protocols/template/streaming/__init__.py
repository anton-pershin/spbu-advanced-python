"""Public API for practicum 7 streaming package."""

from .batching import chunked, consume_batches, count_by_level
from .protocols import BatchConsumer, LineSource
from .service import build_pipeline, load_pipeline, summarize_levels
from .sources import LineIterator, chain_sources, iter_lines, read_lines
from .transforms import LogRecord, filter_by_level, flatten, parse_log_line, parse_records, take

__all__ = [
    "LineSource",
    "BatchConsumer",
    "LineIterator",
    "iter_lines",
    "read_lines",
    "chain_sources",
    "LogRecord",
    "parse_log_line",
    "parse_records",
    "filter_by_level",
    "take",
    "flatten",
    "chunked",
    "count_by_level",
    "consume_batches",
    "build_pipeline",
    "load_pipeline",
    "summarize_levels",
]
