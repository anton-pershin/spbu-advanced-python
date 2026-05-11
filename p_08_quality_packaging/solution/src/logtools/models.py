"""LogRecord data model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LogRecord:
    """Single log record with timestamp, level and message."""

    timestamp: str
    level: str
    message: str
