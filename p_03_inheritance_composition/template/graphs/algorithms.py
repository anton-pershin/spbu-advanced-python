from __future__ import annotations

import heapq
import math
from collections import deque
from typing import Deque, Dict, Iterable, List, Optional, Protocol, Tuple, TypeVar

from .base import Edge

V = TypeVar("V")


class SupportsGraph(Protocol[V]):
    def __contains__(self, vertex: object) -> bool: ...

    def neighbors(self, u: V) -> List[V]: ...

    def iter_edges(self, u: V) -> Iterable[Edge[V]]: ...


def _reconstruct_path(prev: Dict[V, V], src: V, dst: V) -> List[V]:
    out: List[V] = [dst]
    cur = dst
    while cur != src:
        cur = prev[cur]
        out.append(cur)
    out.reverse()
    return out


def bfs_shortest_path(graph: SupportsGraph[V], src: V, dst: V) -> List[V]:
    """Shortest path in an unweighted graph (BFS).

    Returns a list of vertices from src to dst (inclusive).
    Raises KeyError if src or dst is not in graph.
    Raises ValueError if dst is unreachable.
    """

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def dijkstra_shortest_path(
    graph: SupportsGraph[V], src: V, dst: V
) -> Tuple[float, Optional[List[V]]]:
    """Shortest path with non-negative weights (Dijkstra).

    Returns (distance, path). If dst is unreachable, returns (inf, None).
    Raises KeyError if src or dst is not in graph.
    """

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
