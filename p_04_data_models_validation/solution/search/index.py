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
        if not self.doc_id:
            raise ValueError("doc_id must be non-empty")
        if self.term_frequency <= 0:
            raise ValueError("term_frequency must be positive")


@dataclass(frozen=True)
class InvertedIndex:
    postings: Dict[str, Tuple[Posting, ...]]
    document_count: int

    def __post_init__(self) -> None:
        if self.document_count < 0:
            raise ValueError("document_count must be non-negative")

    def document_frequency(self, term: str) -> int:
        return len(self.postings.get(term, ()))


def build_inverted_index(documents: Iterable[Document]) -> InvertedIndex:
    docs = list(documents)
    postings: DefaultDict[str, list[Posting]] = defaultdict(list)

    for doc in docs:
        counts = Counter(doc.tokens)
        for term, frequency in counts.items():
            postings[term].append(Posting(doc_id=doc.doc_id, term_frequency=frequency))

    frozen_postings = {
        term: tuple(sorted(term_postings, key=lambda posting: posting.doc_id))
        for term, term_postings in postings.items()
    }
    return InvertedIndex(postings=frozen_postings, document_count=len(docs))


def search_index(index: InvertedIndex, query: SearchQuery) -> List[SearchResult]:
    scores: Dict[str, float] = {}
    matched_terms: Dict[str, list[str]] = {}

    for term in _unique_terms(query.tokens):
        postings = index.postings.get(term)
        if not postings:
            continue

        idf = math.log((1 + index.document_count) / (1 + len(postings))) + 1.0
        for posting in postings:
            scores[posting.doc_id] = scores.get(posting.doc_id, 0.0) + posting.term_frequency * idf
            matched_terms.setdefault(posting.doc_id, []).append(term)

    results = [
        SearchResult(
            doc_id=doc_id,
            score=score,
            matched_terms=tuple(matched_terms[doc_id]),
        )
        for doc_id, score in scores.items()
    ]
    results.sort(key=lambda result: (-result.score, result.doc_id))
    return results[: query.top_k]
