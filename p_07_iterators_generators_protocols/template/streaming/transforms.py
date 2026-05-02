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
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


def parse_log_line(line: str) -> LogRecord:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def parse_records(lines: Iterable[str]) -> Iterator[LogRecord]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def filter_by_level(records: Iterable[LogRecord], level: str) -> Iterator[LogRecord]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def take(items: Iterable[T], n: int) -> Iterator[T]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def flatten(groups: Iterable[Iterable[T]]) -> Iterator[T]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
