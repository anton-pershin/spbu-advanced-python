from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

from .node import Node

K = TypeVar("K")
V = TypeVar("V")


class DoublyLinkedList(Generic[K, V]):
    def __init__(self) -> None:
        self._head: Node[K, V] = Node(key=None, value=None)
        self._tail: Node[K, V] = Node(key=None, value=None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Node[K, V]]:
        cur = self._head.next
        while cur is not None and cur is not self._tail:
            yield cur
            cur = cur.next

    def _insert_between(self, node: Node[K, V], left: Node[K, V], right: Node[K, V]) -> None:
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node

    def _detach(self, node: Node[K, V]) -> None:
        left = node.prev
        right = node.next
        if left is None or right is None:
            raise RuntimeError("detaching a node not in list")
        left.next = right
        right.prev = left
        node.prev = None
        node.next = None

    def push_front(self, node: Node[K, V]) -> None:
        if node.prev is not None or node.next is not None:
            raise RuntimeError("node already linked")

        assert self._head.next is not None
        self._insert_between(node, self._head, self._head.next)
        self._size += 1

    def remove(self, node: Node[K, V]) -> None:
        self._detach(node)
        self._size -= 1

    def move_to_front(self, node: Node[K, V]) -> None:
        self._detach(node)
        assert self._head.next is not None
        self._insert_between(node, self._head, self._head.next)

    def pop_back(self) -> Optional[Node[K, V]]:
        if self._size == 0:
            return None

        assert self._tail.prev is not None
        node = self._tail.prev
        if node is self._head:
            return None

        self._detach(node)
        self._size -= 1
        return node
