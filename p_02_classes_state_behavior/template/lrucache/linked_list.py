from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

from .node import Node

K = TypeVar("K")
V = TypeVar("V")


class DoublyLinkedList(Generic[K, V]):
    """A doubly linked list with sentinel head/tail.

    The list stores cache entries ordered by recency:
    - front (right after head) is MRU
    - back (right before tail) is LRU

    Required operations must be O(1).
    """

    def __init__(self) -> None:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError

    def __len__(self) -> int:

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError

    def __iter__(self) -> Iterator[Node[K, V]]:
        """Iterate from MRU to LRU."""

        cur = self._head.next
        while cur is not None and cur is not self._tail:
            yield cur
            cur = cur.next

    def push_front(self, node: Node[K, V]) -> None:
        """Insert node right after head (make it MRU)."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError

    def remove(self, node: Node[K, V]) -> None:
        """Remove node from the list."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError

    def move_to_front(self, node: Node[K, V]) -> None:
        """Move existing node to MRU position."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError

    def pop_back(self) -> Optional[Node[K, V]]:
        """Remove and return the LRU node. Return None if empty."""

        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################

        raise NotImplementedError
