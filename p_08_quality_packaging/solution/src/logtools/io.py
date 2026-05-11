"""File I/O operations for log files."""

from __future__ import annotations

from typing import Iterator

from logtools.models import LogRecord


def read_log_file(path: str) -> Iterator[str]:
    """Read log file line by line.

    Args:
        path: Path to log file.

    Yields:
        Stripped log lines.
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def parse_log_line(line: str) -> LogRecord | None:
    """Parse a single log line into LogRecord.

    Args:
        line: Log line in format "timestamp,level,message".

    Returns:
        LogRecord or None if line is invalid.
    """
    parts = line.split(",", 2)
    if len(parts) != 3:
        return None

    timestamp, level, message = parts
    if not timestamp or not level or not message:
        return None

    return LogRecord(timestamp=timestamp, level=level, message=message)
