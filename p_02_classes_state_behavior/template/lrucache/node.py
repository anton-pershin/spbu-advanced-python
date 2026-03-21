from __future__ import annotations

from typing import Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Node(Generic[K, V]):
    """A node in a doubly linked list."""

    def __init__(self, key: Optional[K], value: Optional[V]) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[Node[K, V]] = None
        self.next: Optional[Node[K, V]] = None

    def __repr__(self) -> str:
        return f"Node(key={self.key!r}, value={self.value!r})"
