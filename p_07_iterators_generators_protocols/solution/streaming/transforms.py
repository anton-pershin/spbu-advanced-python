from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from typing import Iterable, Iterator, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class LogRecord:
    timestamp: str
    level: str
    message: str

    def __post_init__(self) -> None:
        if not self.timestamp.strip():
            raise ValueError("timestamp must be non-empty")
        if not self.level.strip():
            raise ValueError("level must be non-empty")
        if not self.message.strip():
            raise ValueError("message must be non-empty")

        object.__setattr__(self, "timestamp", self.timestamp.strip())
        object.__setattr__(self, "level", self.level.strip().upper())
        object.__setattr__(self, "message", self.message.strip())


def parse_log_line(line: str) -> LogRecord:
    parts = [part.strip() for part in line.split(",", 2)]
    if len(parts) != 3 or any(not part for part in parts):
        raise ValueError("log line must contain timestamp, level, and message")
    return LogRecord(timestamp=parts[0], level=parts[1], message=parts[2])


def parse_records(lines: Iterable[str]) -> Iterator[LogRecord]:
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            yield parse_log_line(stripped)
        except ValueError:
            continue


def filter_by_level(records: Iterable[LogRecord], level: str) -> Iterator[LogRecord]:
    normalized = level.strip().upper()
    if not normalized:
        raise ValueError("level must be non-empty")

    for record in records:
        if record.level == normalized:
            yield record


def take(items: Iterable[T], n: int) -> Iterator[T]:
    if n < 0:
        raise ValueError("n must be non-negative")
    yield from islice(items, n)


def flatten(groups: Iterable[Iterable[T]]) -> Iterator[T]:
    for group in groups:
        yield from group
