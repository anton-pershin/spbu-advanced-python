from __future__ import annotations

from typing import Dict, Generic, List, Optional, Tuple, TypeVar

from .linked_list import DoublyLinkedList
from .node import Node

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if not isinstance(capacity, int) or isinstance(capacity, bool):
            raise TypeError("capacity must be an int")
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self.capacity = capacity
        self._list: DoublyLinkedList[K, V] = DoublyLinkedList()
        self._nodes: Dict[K, Node[K, V]] = {}

    def __len__(self) -> int:
        return len(self._nodes)

    def __contains__(self, key: object) -> bool:
        return key in self._nodes

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        node = self._nodes.get(key)
        if node is None:
            return default

        self._list.move_to_front(node)
        # node.value is Optional[V] for sentinel compatibility, but real cache nodes always have V
        return node.value  # type: ignore[return-value]

    def put(self, key: K, value: V) -> None:
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._list.move_to_front(node)
            return

        node = Node(key=key, value=value)
        self._list.push_front(node)
        self._nodes[key] = node

        if len(self._nodes) > self.capacity:
            lru = self._list.pop_back()
            if lru is None or lru.key is None:
                raise RuntimeError("internal error: expected a real node to evict")
            del self._nodes[lru.key]

    def items(self) -> List[Tuple[K, V]]:
        out: List[Tuple[K, V]] = []
        for node in self._list:
            if node.key is None:
                continue
            out.append((node.key, node.value))  # type: ignore[arg-type]
        return out

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={self.items()!r})"
