from __future__ import annotations

from collections.abc import Iterable, Iterator

from .protocols import LineSource


class LineIterator(Iterator[str]):
    def __init__(self, lines: Iterable[str]) -> None:
        self._iterator = iter(lines)

    def __iter__(self) -> "LineIterator":
        return self

    def __next__(self) -> str:
        return next(self._iterator).rstrip("\n")


def iter_lines(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        yield line.rstrip("\n")


def read_lines(path: str, *, encoding: str = "utf-8") -> Iterator[str]:
    with open(path, encoding=encoding) as file:
        for line in file:
            yield line.rstrip("\n")


def chain_sources(sources: Iterable[LineSource]) -> Iterator[str]:
    for source in sources:
        yield from source
