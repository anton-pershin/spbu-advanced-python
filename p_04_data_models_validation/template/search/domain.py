from __future__ import annotations

import re
from dataclasses import dataclass

TOKEN_RE = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")


def tokenize(text: str) -> tuple[str, ...]:
    """Lowercase text and extract alphanumeric tokens."""

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


@dataclass(frozen=True)
class Document:
    doc_id: str
    tokens: tuple[str, ...]

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


@dataclass(frozen=True)
class SearchQuery:
    tokens: tuple[str, ...]
    top_k: int

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


@dataclass(frozen=True)
class SearchResult:
    doc_id: str
    score: float
    matched_terms: tuple[str, ...]

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError
