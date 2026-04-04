"""Lightweight checks (no pytest yet).

Run from repo root:

python -m p_04_data_models_validation.template.check

The checks intentionally use only the public API:

from p_04_data_models_validation.template.search import ...
"""

from __future__ import annotations

from pydantic import ValidationError

from p_04_data_models_validation.template.search import (
    Document,
    DocumentIn,
    DocumentPayload,
    QueryPayload,
    SearchEngine,
    SearchQuery,
    build_inverted_index,
    search_index,
    tokenize,
)


def test_pydantic_validation() -> None:
    ok = DocumentIn.model_validate({"id": "d1", "text": "Graph search"})
    assert ok.id == "d1"

    try:
        DocumentIn.model_validate({"id": "d2", "text": "   "})
    except ValidationError:
        pass
    else:
        raise AssertionError("empty text must be rejected")


def test_domain_invariants() -> None:
    try:
        Document(doc_id="", tokens=("graph",))
    except ValueError:
        pass
    else:
        raise AssertionError("empty doc_id must be rejected")

    try:
        SearchQuery(tokens=(), top_k=3)
    except ValueError:
        pass
    else:
        raise AssertionError("empty query tokens must be rejected")


def test_inverted_index_building() -> None:
    docs = [
        Document(doc_id="d1", tokens=("graph", "graph", "path")),
        Document(doc_id="d2", tokens=("path", "cache")),
    ]
    index = build_inverted_index(docs)

    assert index.document_count == 2
    assert index.document_frequency("graph") == 1
    assert index.document_frequency("path") == 2

    graph_postings = index.postings["graph"]
    assert len(graph_postings) == 1
    assert graph_postings[0].doc_id == "d1"
    assert graph_postings[0].term_frequency == 2


def test_search_scoring_and_order() -> None:
    docs = [
        Document(doc_id="d1", tokens=tokenize("graph shortest path bfs")),
        Document(doc_id="d2", tokens=tokenize("graph graph path")),
        Document(doc_id="d3", tokens=tokenize("cache eviction policy")),
    ]
    index = build_inverted_index(docs)
    query = SearchQuery(tokens=tokenize("graph path graph"), top_k=2)

    results = search_index(index, query)

    assert [result.doc_id for result in results] == ["d2", "d1"]
    assert results[0].score > results[1].score
    assert results[0].matched_terms == ("graph", "path")


def test_search_engine_api() -> None:
    payloads: list[DocumentPayload] = [
        {"id": "d1", "text": "graph path graph"},
        {"id": "d2", "text": "cache eviction policy"},
        {"id": "d3", "text": "graph shortest path"},
    ]
    engine = SearchEngine.from_payloads(payloads, default_top_k=2)

    query: QueryPayload = {"text": "graph path"}
    results = engine.search(query)
    assert len(results) == 2
    assert [result.doc_id for result in results] == ["d1", "d3"]

    engine.default_top_k = 1
    one_result = engine.search({"text": "graph"})
    assert len(one_result) == 1

    try:
        engine.default_top_k = 0
    except ValueError:
        pass
    else:
        raise AssertionError("default_top_k must be positive")


def main() -> int:
    tests = [
        test_pydantic_validation,
        test_domain_invariants,
        test_inverted_index_building,
        test_search_scoring_and_order,
        test_search_engine_api,
    ]

    for t in tests:
        t()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
