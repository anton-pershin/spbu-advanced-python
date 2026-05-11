"""Tests for log I/O operations."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from logtools.io import parse_log_line, read_log_file
from logtools.models import LogRecord


def test_parse_valid_line() -> None:
    """Test parsing a valid log line."""
    line = "2024-05-01T10:00:00,INFO,worker started"
    record = parse_log_line(line)
    assert record == LogRecord(
        timestamp="2024-05-01T10:00:00",
        level="INFO",
        message="worker started",
    )


def test_parse_invalid_line() -> None:
    """Test parsing an invalid log line."""
    assert parse_log_line("broken line") is None
    assert parse_log_line("") is None
    assert parse_log_line("a,b") is None


def test_read_file() -> None:
    """Test reading a log file."""
    with TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "test.log"
        path.write_text("line1\nline2\nline3\n", encoding="utf-8")
        assert list(read_log_file(str(path))) == ["line1", "line2", "line3"]
