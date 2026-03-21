from __future__ import annotations

from typing import Dict, Generic, List, Optional, Tuple, TypeVar

from .linked_list import DoublyLinkedList
from .node import Node

K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def __len__(self) -> int:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def __contains__(self, key: object) -> bool:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def put(self, key: K, value: V) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def items(self) -> List[Tuple[K, V]]:
        """Return items ordered from MRU to LRU."""
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, items={self.items()!r})"
