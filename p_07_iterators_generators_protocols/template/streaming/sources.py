from __future__ import annotations

from collections.abc import Iterable, Iterator

from .protocols import LineSource


class LineIterator(Iterator[str]):
    def __init__(self, lines: Iterable[str]) -> None:
        self._iterator = iter(lines)

    def __iter__(self) -> "LineIterator":
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def __next__(self) -> str:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


def iter_lines(lines: Iterable[str]) -> Iterator[str]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def read_lines(path: str, *, encoding: str = "utf-8") -> Iterator[str]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def chain_sources(sources: Iterable[LineSource]) -> Iterator[str]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
