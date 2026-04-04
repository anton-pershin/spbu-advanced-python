from __future__ import annotations

import re
from dataclasses import dataclass

TOKEN_RE = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")


def tokenize(text: str) -> tuple[str, ...]:
    """Lowercase text and extract alphanumeric tokens."""

    return tuple(token.lower() for token in TOKEN_RE.findall(text))


@dataclass(frozen=True)
class Document:
    doc_id: str
    tokens: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.doc_id:
            raise ValueError("doc_id must be non-empty")
        if not self.tokens:
            raise ValueError("document must contain at least one token")


@dataclass(frozen=True)
class SearchQuery:
    tokens: tuple[str, ...]
    top_k: int

    def __post_init__(self) -> None:
        if not self.tokens:
            raise ValueError("query must contain at least one token")
        if self.top_k <= 0:
            raise ValueError("top_k must be positive")


@dataclass(frozen=True)
class SearchResult:
    doc_id: str
    score: float
    matched_terms: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.doc_id:
            raise ValueError("doc_id must be non-empty")
        if self.score < 0:
            raise ValueError("score must be non-negative")
        if not self.matched_terms:
            raise ValueError("matched_terms must be non-empty")
