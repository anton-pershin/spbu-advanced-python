"""Lightweight checks (no pytest yet).

Run from repo root:

python -m p_03_inheritance_composition.template.check

The checks intentionally use only the public API:

from p_03_inheritance_composition.template.graphs import ...
"""

from __future__ import annotations

import math

from p_03_inheritance_composition.template.graphs import (
    DirectedMixin,
    Graph,
    GraphBase,
    UndirectedMixin,
    UnweightedMixin,
    WeightedMixin,
    bfs_shortest_path,
    dijkstra_shortest_path,
)


class UnweightedUndirectedGraph(UnweightedMixin, UndirectedMixin, GraphBase[str]):
    pass


class UnweightedUndirectedGraphAlt(UndirectedMixin, UnweightedMixin, GraphBase[str]):
    pass


class WeightedDirectedGraph(WeightedMixin, DirectedMixin, GraphBase[str]):
    pass


def test_unweighted_undirected_add_edge_and_bfs() -> None:
    g = UnweightedUndirectedGraph()

    g.add_edge("a", "b")
    g.add_edge("b", "c")
    g.add_edge("a", "d")
    g.add_edge("d", "c")

    # Undirected: both directions exist.
    assert set(g.neighbors("a")) == {"b", "d"}
    assert set(g.neighbors("b")) == {"a", "c"}

    # Unweighted: explicit weights forbidden.
    try:
        g.add_edge("a", "x", weight=123)
    except ValueError:
        pass
    else:
        raise AssertionError("unweighted graph must reject explicit weights")

    path = bfs_shortest_path(g, "a", "c")
    assert path in (["a", "b", "c"], ["a", "d", "c"])  # two valid shortest paths


def test_mro_cooperation_same_behavior() -> None:
    g1 = UnweightedUndirectedGraph()
    g2 = UnweightedUndirectedGraphAlt()

    edges = [("a", "b"), ("b", "c"), ("c", "d")]
    for u, v in edges:
        g1.add_edge(u, v)
        g2.add_edge(u, v)

    for v in ["a", "b", "c", "d"]:
        assert set(g1.neighbors(v)) == set(g2.neighbors(v))


def test_weighted_directed_dijkstra() -> None:
    g = WeightedDirectedGraph()

    # A small directed weighted graph.
    g.add_edge("s", "a", weight=2)
    g.add_edge("s", "b", weight=5)
    g.add_edge("a", "b", weight=1)
    g.add_edge("a", "t", weight=7)
    g.add_edge("b", "t", weight=1)

    dist, path = dijkstra_shortest_path(g, "s", "t")
    assert dist == 4
    assert path == ["s", "a", "b", "t"]

    # Weighted: missing weight forbidden.
    try:
        g.add_edge("x", "y")
    except ValueError:
        pass
    else:
        raise AssertionError("weighted graph must require weight")

    # Dijkstra requires non-negative weights.
    try:
        g.add_edge("t", "x", weight=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative weights must be rejected")


def test_composition_graph_matches_variants() -> None:
    # Unweighted undirected via composition.
    g = Graph[str](directed=False, weighted=False)
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    assert bfs_shortest_path(g, "a", "c") == ["a", "b", "c"]

    # Weighted directed via composition.
    w = Graph[str](directed=True, weighted=True)
    w.add_edge("s", "a", weight=2)
    w.add_edge("a", "t", weight=1)
    dist, path = dijkstra_shortest_path(w, "s", "t")
    assert dist == 3
    assert path == ["s", "a", "t"]

    # Unreachable.
    dist2, path2 = dijkstra_shortest_path(w, "t", "s")
    assert dist2 == math.inf
    assert path2 is None


def main() -> int:
    tests = [
        test_unweighted_undirected_add_edge_and_bfs,
        test_mro_cooperation_same_behavior,
        test_weighted_directed_dijkstra,
        test_composition_graph_matches_variants,
    ]

    for t in tests:
        t()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
