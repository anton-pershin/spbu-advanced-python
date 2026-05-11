"""Tests for statistics operations."""

from __future__ import annotations

from logtools.models import LogRecord
from logtools.stats import count_by_level, top_messages


def test_count_by_level() -> None:
    """Test counting records by level."""
    records = [
        LogRecord("t1", "INFO", "msg1"),
        LogRecord("t2", "ERROR", "msg2"),
        LogRecord("t3", "INFO", "msg3"),
        LogRecord("t4", "ERROR", "msg4"),
        LogRecord("t5", "ERROR", "msg5"),
    ]
    assert count_by_level(records) == {"INFO": 2, "ERROR": 3}


def test_top_messages() -> None:
    """Test getting top N messages."""
    records = [
        LogRecord("t1", "INFO", "common"),
        LogRecord("t2", "INFO", "common"),
        LogRecord("t3", "INFO", "common"),
        LogRecord("t4", "ERROR", "rare1"),
        LogRecord("t5", "ERROR", "rare2"),
    ]
    assert top_messages(records, 2) == [("common", 3), ("rare1", 1)]


def test_top_messages_sorting() -> None:
    """Test that top_messages sorts by count desc, then message asc."""
    records = [
        LogRecord("t1", "INFO", "b"),
        LogRecord("t2", "INFO", "b"),
        LogRecord("t3", "INFO", "a"),
        LogRecord("t4", "INFO", "a"),
        LogRecord("t5", "INFO", "c"),
    ]
    assert top_messages(records, 3) == [("a", 2), ("b", 2), ("c", 1)]
