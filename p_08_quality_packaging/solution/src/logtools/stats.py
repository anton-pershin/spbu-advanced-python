"""Statistics operations on log records."""

from __future__ import annotations

from collections import Counter
from typing import Iterable

from logtools.models import LogRecord


def count_by_level(records: Iterable[LogRecord]) -> dict[str, int]:
    """Count log records by level.

    Args:
        records: Iterable of log records.

    Returns:
        Dictionary mapping level to count.
    """
    counter = Counter(record.level for record in records)
    return dict(counter)


def top_messages(records: Iterable[LogRecord], n: int = 10) -> list[tuple[str, int]]:
    """Get top N most frequent messages.

    Args:
        records: Iterable of log records.
        n: Number of top messages to return.

    Returns:
        List of (message, count) tuples sorted by count desc, then message asc.
    """
    counter = Counter(record.message for record in records)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
