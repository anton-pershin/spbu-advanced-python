from __future__ import annotations

from typing import Iterable, List

from .domain import Document, SearchQuery, SearchResult, tokenize
from .external import DocumentIn, DocumentPayload, QueryIn, QueryPayload
from .index import InvertedIndex, build_inverted_index, search_index


def parse_documents(payloads: Iterable[DocumentPayload]) -> List[Document]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def parse_query(payload: QueryPayload, *, default_top_k: int) -> SearchQuery:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


class SearchEngine:
    def __init__(self, documents: Iterable[Document], *, default_top_k: int = 5) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    @property
    def documents(self) -> tuple[Document, ...]:
        return self._documents

    @property
    def index(self) -> InvertedIndex:
        return self._index

    @property
    def default_top_k(self) -> int:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    @default_top_k.setter
    def default_top_k(self, value: int) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    @classmethod
    def from_payloads(
        cls, payloads: Iterable[DocumentPayload], *, default_top_k: int = 5
    ) -> "SearchEngine":
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def search(self, payload: QueryPayload) -> List[SearchResult]:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


def build_search_engine(
    payloads: Iterable[DocumentPayload], *, default_top_k: int = 5
) -> SearchEngine:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def search_documents(engine: SearchEngine, query_payload: QueryPayload) -> List[SearchResult]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
