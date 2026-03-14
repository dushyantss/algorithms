from . import doubly_linked_list


class Dequeue(doubly_linked_list.DoublyLinkedList):
    def peek_front(self):
        if self._head is None:
            raise IndexError("Dequeue is empty")
        return self._head.value

    def peek_back(self):
        if self._tail is None:
            raise IndexError("Dequeue is empty")
        return self._tail.value
