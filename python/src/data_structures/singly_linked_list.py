from collections.abc import MutableSequence
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(kw_only=True)
class SinglyLinkedNode:
    value: Any
    next: Optional["SinglyLinkedNode"]


class SinglyLinkedList(MutableSequence):
    def __init__(self):
        self._head: SinglyLinkedNode | None = None
        self._size: int = 0

    def __iter__(self):
        for node in self._iter_nodes():
            yield node.value

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int | slice):
        self._discard_slice_index(index)

        index = self._validated_index(index)
        for i, value in enumerate(self):
            if i == index:
                return value

    def __setitem__(self, index: int | slice, value):
        self._discard_slice_index(index)

        index = self._validated_index(index)
        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                node.value = value
                return

    def __delitem__(self, index: int | slice):
        self._discard_slice_index(index)
        index = self._validated_index(index)

        prev = None
        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                if prev is None:
                    self._head = node.next
                else:
                    prev.next = node.next

                self._size -= 1
                return
            else:
                prev = node

    def insert(self, index: int, value):
        if index < 0:
            index += self._size

        if index <= 0:
            index = 0
        elif index >= self._size:
            index = self._size

        prev: SinglyLinkedList | None = None
        next: SinglyLinkedNode | None = None
        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                next = node
                break

            else:
                prev = node

        if prev is None:
            self._head = SinglyLinkedNode(value=value, next=next)
        else:
            prev.next = SinglyLinkedNode(value=value, next=next)

        self._size += 1

    def _discard_slice_index(self, index):
        if isinstance(index, slice):
            raise NotImplementedError("Slicing is not supported")

    def _validated_index(self, index):
        if index < 0:
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        return index

    def _iter_nodes(self):
        node = self._head
        while node is not None:
            yield node
            node = node.next
