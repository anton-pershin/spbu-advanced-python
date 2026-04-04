from __future__ import annotations

from typing import Iterable, List

from .domain import Document, SearchQuery, SearchResult, tokenize
from .external import DocumentIn, DocumentPayload, QueryIn, QueryPayload
from .index import InvertedIndex, build_inverted_index, search_index


def parse_documents(payloads: Iterable[DocumentPayload]) -> List[Document]:
    documents: list[Document] = []
    for payload in payloads:
        model = DocumentIn.model_validate(payload)
        documents.append(Document(doc_id=model.id, tokens=tokenize(model.text)))
    return documents


def parse_query(payload: QueryPayload, *, default_top_k: int) -> SearchQuery:
    merged_payload = {"top_k": default_top_k, **payload}
    model = QueryIn.model_validate(merged_payload)
    return SearchQuery(tokens=tokenize(model.text), top_k=model.top_k)


class SearchEngine:
    def __init__(self, documents: Iterable[Document], *, default_top_k: int = 5) -> None:
        docs = tuple(documents)
        if not docs:
            raise ValueError("search engine requires at least one document")

        doc_ids = [doc.doc_id for doc in docs]
        if len(set(doc_ids)) != len(doc_ids):
            raise ValueError("document ids must be unique")

        self._documents = docs
        self._index = build_inverted_index(docs)
        self.default_top_k = default_top_k

    @property
    def documents(self) -> tuple[Document, ...]:
        return self._documents

    @property
    def index(self) -> InvertedIndex:
        return self._index

    @property
    def default_top_k(self) -> int:
        return self._default_top_k

    @default_top_k.setter
    def default_top_k(self, value: int) -> None:
        if value <= 0:
            raise ValueError("default_top_k must be positive")
        self._default_top_k = value

    @classmethod
    def from_payloads(
        cls, payloads: Iterable[DocumentPayload], *, default_top_k: int = 5
    ) -> "SearchEngine":
        return cls(parse_documents(payloads), default_top_k=default_top_k)

    def search(self, payload: QueryPayload) -> List[SearchResult]:
        query = parse_query(payload, default_top_k=self.default_top_k)
        return search_index(self.index, query)


def build_search_engine(
    payloads: Iterable[DocumentPayload], *, default_top_k: int = 5
) -> SearchEngine:
    return SearchEngine.from_payloads(payloads, default_top_k=default_top_k)


def search_documents(engine: SearchEngine, query_payload: QueryPayload) -> List[SearchResult]:
    return engine.search(query_payload)
