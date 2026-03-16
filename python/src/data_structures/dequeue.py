from . import doubly_linked_list


class Dequeue(doubly_linked_list.DoublyLinkedList):
    """Double-ended queue built on top of `DoublyLinkedList`.

    A deque supports efficient insertion and removal from both ends. It is
    useful for BFS, sliding-window problems, palindrome checks, and task
    scheduling where both ends matter.
    """

    def peek_front(self):
        if self._head is None:
            raise IndexError("Dequeue is empty")
        return self._head.value

    def peek_back(self):
        if self._tail is None:
            raise IndexError("Dequeue is empty")
        return self._tail.value
