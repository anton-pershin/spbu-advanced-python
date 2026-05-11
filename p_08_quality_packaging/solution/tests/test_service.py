"""Tests for high-level service."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from logtools.models import LogRecord
from logtools.service import analyze_log, filter_by_level


def test_filter_by_level() -> None:
    """Test filtering records by level."""
    records = [
        LogRecord("t1", "INFO", "msg1"),
        LogRecord("t2", "ERROR", "msg2"),
        LogRecord("t3", "INFO", "msg3"),
        LogRecord("t4", "ERROR", "msg4"),
    ]
    errors = filter_by_level(records, "error")
    assert len(errors) == 2
    assert all(r.level == "ERROR" for r in errors)


def test_analyze_log() -> None:
    """Test full log analysis."""
    with TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "test.log"
        path.write_text(
            "2024-05-01T10:00:00,INFO,msg1\n"
            "2024-05-01T10:01:00,ERROR,msg2\n"
            "2024-05-01T10:02:00,INFO,msg1\n",
            encoding="utf-8",
        )
        result = analyze_log(str(path))
        assert result["level_counts"] == {"INFO": 2, "ERROR": 1}
        assert result["top_messages"] == [("msg1", 2), ("msg2", 1)]


def test_analyze_log_with_filter() -> None:
    """Test log analysis with level filter."""
    with TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "test.log"
        path.write_text(
            "2024-05-01T10:00:00,INFO,msg1\n"
            "2024-05-01T10:01:00,ERROR,msg2\n"
            "2024-05-01T10:02:00,INFO,msg3\n",
            encoding="utf-8",
        )
        result = analyze_log(str(path), level="ERROR")
        assert result["level_counts"] == {"ERROR": 1}
        assert result["top_messages"] == [("msg2", 1)]
