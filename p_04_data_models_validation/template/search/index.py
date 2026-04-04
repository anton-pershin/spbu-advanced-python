from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Dict, Iterable, List, Tuple

from .domain import Document, SearchQuery, SearchResult


def _unique_terms(tokens: tuple[str, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    out: list[str] = []
    for token in tokens:
        if token not in seen:
            seen.add(token)
            out.append(token)
    return tuple(out)


@dataclass(frozen=True)
class Posting:
    doc_id: str
    term_frequency: int

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


@dataclass(frozen=True)
class InvertedIndex:
    postings: Dict[str, Tuple[Posting, ...]]
    document_count: int

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def document_frequency(self, term: str) -> int:
        return len(self.postings.get(term, ()))


def build_inverted_index(documents: Iterable[Document]) -> InvertedIndex:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def search_index(index: InvertedIndex, query: SearchQuery) -> List[SearchResult]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
