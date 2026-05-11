"""High-level service for log analysis."""

from __future__ import annotations

from typing import Iterable

from logtools.io import parse_log_line, read_log_file
from logtools.models import LogRecord
from logtools.stats import count_by_level, top_messages


def filter_by_level(records: Iterable[LogRecord], level: str) -> list[LogRecord]:
    """Filter records by level.

    Args:
        records: Iterable of log records.
        level: Level to filter by (case-insensitive).

    Returns:
        List of records matching the level.
    """
    level_upper = level.upper()
    return [record for record in records if record.level == level_upper]


def analyze_log(
    path: str, level: str | None = None, top_n: int = 10
) -> dict[str, object]:
    """Analyze log file and return summary.

    Args:
        path: Path to log file.
        level: Optional level to filter by.
        top_n: Number of top messages to include.

    Returns:
        Dictionary with 'level_counts' and 'top_messages' keys.
    """
    records = []
    for line in read_log_file(path):
        record = parse_log_line(line)
        if record is not None:
            records.append(record)

    if level is not None:
        records = filter_by_level(records, level)

    return {
        "level_counts": count_by_level(records),
        "top_messages": top_messages(records, top_n),
    }
