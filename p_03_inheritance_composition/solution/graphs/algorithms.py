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
    if src not in graph:
        raise KeyError(src)
    if dst not in graph:
        raise KeyError(dst)
    if src == dst:
        return [src]

    q: Deque[V] = deque([src])
    prev: Dict[V, V] = {}
    seen = {src}

    while q:
        u = q.popleft()
        for v in graph.neighbors(u):
            if v in seen:
                continue
            seen.add(v)
            prev[v] = u
            if v == dst:
                return _reconstruct_path(prev, src, dst)
            q.append(v)

    raise ValueError("destination is unreachable")


def dijkstra_shortest_path(
    graph: SupportsGraph[V], src: V, dst: V
) -> Tuple[float, Optional[List[V]]]:
    if src not in graph:
        raise KeyError(src)
    if dst not in graph:
        raise KeyError(dst)
    if src == dst:
        return (0.0, [src])

    dist: Dict[V, float] = {src: 0.0}
    prev: Dict[V, V] = {}
    pq: List[Tuple[float, V]] = [(0.0, src)]

    while pq:
        du, u = heapq.heappop(pq)
        if du != dist.get(u, math.inf):
            continue
        if u == dst:
            return (du, _reconstruct_path(prev, src, dst))

        for e in graph.iter_edges(u):
            edge: Edge[V] = e
            v = edge.to
            w = float(edge.weight)
            nd = du + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return (math.inf, None)
