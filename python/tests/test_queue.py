import pytest
from data_structures.queue import Queue


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_queue(*values) -> Queue:
    """Convenience: create a Queue pre-populated with values via enqueue."""
    q = Queue()
    for v in values:
        q.enqueue(v)
    return q


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        q = Queue()
        assert len(q) == 0


# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_enqueue(self):
        q = Queue()
        q.enqueue(1)
        assert len(q) == 1

    def test_len_decreases_on_dequeue(self):
        q = make_queue(1, 2, 3)
        q.dequeue()
        assert len(q) == 2

    def test_len_after_multiple_enqueues(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        assert len(q) == 5


# ---------------------------------------------------------------------------
# enqueue
# ---------------------------------------------------------------------------

class TestEnqueue:
    def test_enqueue_increases_length(self):
        q = Queue()
        q.enqueue(1)
        assert len(q) == 1

    def test_enqueue_makes_value_accessible_via_peek(self):
        q = Queue()
        q.enqueue(1)
        assert q.peek() == 1

    def test_enqueue_adds_to_back(self):
        # The first enqueued item must remain at the front
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.peek() == 1

    def test_enqueue_multiple(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert len(q) == 3


# ---------------------------------------------------------------------------
# dequeue
# ---------------------------------------------------------------------------

class TestDequeue:
    def test_dequeue_returns_first_element(self):
        q = make_queue(1, 2, 3)
        assert q.dequeue() == 1

    def test_dequeue_removes_first_element(self):
        q = make_queue(1, 2, 3)
        q.dequeue()
        assert q.peek() == 2

    def test_dequeue_decreases_length(self):
        q = make_queue(1, 2, 3)
        q.dequeue()
        assert len(q) == 2

    def test_dequeue_fifo_order(self):
        # Elements must come out in first-in-first-out order
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_dequeue_empties_queue(self):
        q = make_queue(1)
        q.dequeue()
        assert len(q) == 0

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_dequeue_until_empty_then_raises(self):
        q = make_queue(1)
        q.dequeue()
        with pytest.raises(IndexError):
            q.dequeue()


# ---------------------------------------------------------------------------
# peek
# ---------------------------------------------------------------------------

class TestPeek:
    def test_peek_returns_first_element(self):
        q = make_queue(1, 2, 3)
        assert q.peek() == 1

    def test_peek_does_not_remove_element(self):
        q = make_queue(1, 2, 3)
        q.peek()
        assert len(q) == 3

    def test_peek_same_value_on_repeated_calls(self):
        q = make_queue(1, 2, 3)
        assert q.peek() == q.peek()

    def test_peek_updates_after_dequeue(self):
        q = make_queue(1, 2, 3)
        q.dequeue()
        assert q.peek() == 2

    def test_peek_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.peek()


# ---------------------------------------------------------------------------
# enqueue/dequeue interleaved
# ---------------------------------------------------------------------------

class TestInterleaved:
    def test_enqueue_dequeue_alternating(self):
        q = Queue()
        q.enqueue(1)
        assert q.dequeue() == 1
        q.enqueue(2)
        assert q.dequeue() == 2
        assert len(q) == 0

    def test_enqueue_after_emptying(self):
        q = make_queue(1, 2)
        q.dequeue()
        q.dequeue()
        q.enqueue(3)
        assert q.peek() == 3
        assert len(q) == 1

    def test_fifo_order_with_interleaved_operations(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert len(q) == 0

    def test_peek_consistent_during_interleaved_operations(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.peek() == 1
        q.dequeue()
        assert q.peek() == 2
        q.enqueue(3)
        assert q.peek() == 2