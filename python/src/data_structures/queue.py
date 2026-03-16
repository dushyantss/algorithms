"""A FIFO queue built on top of the double-ended queue implementation.

Queues are used when the oldest item should be processed first. They appear in
BFS, task scheduling, buffering, producer-consumer pipelines, and simulations.
"""

from data_structures.dequeue import Dequeue


class Queue(Dequeue):
    """Queue interface exposing only front-removal and back-insertion.

    Inheriting from `Dequeue` lets the queue reuse O(1) operations at both
    ends while presenting the narrower FIFO API users expect.
    """

    def enqueue(self, value):
        """Add a value to the back of the queue."""
        self.push_back(value)

    def dequeue(self):
        """Remove and return the value at the front of the queue."""
        return self.pop_front()

    def peek(self):
        """Return the next value to be dequeued without removing it."""
        return self.peek_front()
