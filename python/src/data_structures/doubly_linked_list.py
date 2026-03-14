from collections.abc import MutableSequence
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(kw_only=True)
class DoublyLinkedNode:
    value: Any
    next: Optional["DoublyLinkedNode"]
    prev: Optional["DoublyLinkedNode"]


class SinglyLinkedList(MutableSequence):
    def __init__(self):
        self._head: DoublyLinkedNode | None = None
        self._tail: DoublyLinkedNode | None = None
        self._size: int = 0

    def __iter__(self):
        for node in self._iter_nodes():
            yield node.value

    def __reversed__(self):
        node = self._tail
        while node is not None:
            yield node.value
            node = node.prev

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

        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                if node.prev is None:
                    self._head = node.next
                else:
                    node.prev.next = node.next

                if node.next is None:
                    self._tail = node.prev
                else:
                    node.next.prev = node.prev

                self._size -= 1
                return

    def insert(self, index: int, value):
        if index < 0:
            index += self._size

        if index <= 0:
            index = 0
        elif index >= self._size:
            index = self._size

        current_node: DoublyLinkedNode | None = None
        for i, node in enumerate(self._iter_nodes()):
            current_node = node
            if i == index:
                break

        if current_node is None:
            self._head = DoublyLinkedNode(value=value, next=None, prev=None)
            self._tail = self._head
        elif index == 0:
            self._head = DoublyLinkedNode(value=value, next=current_node, prev=None)
            current_node.prev = self._head
        elif index == self._size:
            self._tail = DoublyLinkedNode(value=value, next=None, prev=current_node)
            current_node.next = self._tail
        else:
            node = DoublyLinkedNode(
                value=value, next=current_node, prev=current_node.prev
            )
            current_node.prev.next = node
            current_node.prev = node

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
