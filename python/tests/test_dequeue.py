import pytest
from data_structures.dequeue import Dequeue


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_dequeue(*values) -> Dequeue:
    """Convenience: create a Dequeue pre-populated with values via push_back."""
    dq = Dequeue()
    for v in values:
        dq.push_back(v)
    return dq


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        dq = Dequeue()
        assert len(dq) == 0


# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_push_back(self):
        dq = Dequeue()
        dq.push_back(1)
        assert len(dq) == 1

    def test_len_increases_on_push_front(self):
        dq = Dequeue()
        dq.push_front(1)
        assert len(dq) == 1

    def test_len_decreases_on_pop_back(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert len(dq) == 2

    def test_len_decreases_on_pop_front(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert len(dq) == 2


# ---------------------------------------------------------------------------
# push_front
# ---------------------------------------------------------------------------

class TestPushFront:
    def test_push_front_adds_to_beginning(self):
        dq = make_dequeue(2, 3)
        dq.push_front(1)
        assert list(dq) == [1, 2, 3]

    def test_push_front_increases_length(self):
        dq = make_dequeue(1, 2)
        dq.push_front(0)
        assert len(dq) == 3

    def test_push_front_onto_empty(self):
        dq = Dequeue()
        dq.push_front(1)
        assert list(dq) == [1]

    def test_push_front_onto_empty_peek_front(self):
        dq = Dequeue()
        dq.push_front(1)
        assert dq.peek_front() == 1

    def test_push_front_onto_empty_peek_back(self):
        # When pushing onto an empty dequeue, both ends point to the same node
        dq = Dequeue()
        dq.push_front(1)
        assert dq.peek_back() == 1

    def test_push_front_updates_peek_front(self):
        dq = make_dequeue(2, 3)
        dq.push_front(1)
        assert dq.peek_front() == 1

    def test_push_front_does_not_change_peek_back(self):
        dq = make_dequeue(1, 2)
        dq.push_front(0)
        assert dq.peek_back() == 2

    def test_push_front_multiple(self):
        dq = Dequeue()
        dq.push_front(3)
        dq.push_front(2)
        dq.push_front(1)
        assert list(dq) == [1, 2, 3]


# ---------------------------------------------------------------------------
# push_back
# ---------------------------------------------------------------------------

class TestPushBack:
    def test_push_back_adds_to_end(self):
        dq = make_dequeue(1, 2)
        dq.push_back(3)
        assert list(dq) == [1, 2, 3]

    def test_push_back_increases_length(self):
        dq = make_dequeue(1, 2)
        dq.push_back(3)
        assert len(dq) == 3

    def test_push_back_onto_empty(self):
        dq = Dequeue()
        dq.push_back(1)
        assert list(dq) == [1]

    def test_push_back_onto_empty_peek_back(self):
        dq = Dequeue()
        dq.push_back(1)
        assert dq.peek_back() == 1

    def test_push_back_onto_empty_peek_front(self):
        # When pushing onto an empty dequeue, both ends point to the same node
        dq = Dequeue()
        dq.push_back(1)
        assert dq.peek_front() == 1

    def test_push_back_updates_peek_back(self):
        dq = make_dequeue(1, 2)
        dq.push_back(3)
        assert dq.peek_back() == 3

    def test_push_back_does_not_change_peek_front(self):
        dq = make_dequeue(1, 2)
        dq.push_back(3)
        assert dq.peek_front() == 1

    def test_push_back_multiple(self):
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        dq.push_back(3)
        assert list(dq) == [1, 2, 3]


# ---------------------------------------------------------------------------
# pop_front
# ---------------------------------------------------------------------------

class TestPopFront:
    def test_pop_front_returns_first_element(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.pop_front() == 1

    def test_pop_front_removes_first_element(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert list(dq) == [2, 3]

    def test_pop_front_decreases_length(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert len(dq) == 2

    def test_pop_front_updates_peek_front(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert dq.peek_front() == 2

    def test_pop_front_does_not_change_peek_back(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert dq.peek_back() == 3

    def test_pop_front_single_element_empties_dequeue(self):
        dq = make_dequeue(1)
        dq.pop_front()
        assert len(dq) == 0

    def test_pop_front_single_element_peek_front_raises(self):
        # After popping the last element, peek_front must raise
        dq = make_dequeue(1)
        dq.pop_front()
        with pytest.raises(IndexError):
            dq.peek_front()

    def test_pop_front_single_element_peek_back_raises(self):
        # After popping the last element, peek_back must also raise
        dq = make_dequeue(1)
        dq.pop_front()
        with pytest.raises(IndexError):
            dq.peek_back()

    def test_pop_front_empty_raises(self):
        dq = Dequeue()
        with pytest.raises(IndexError):
            dq.pop_front()

    def test_pop_front_fifo_order(self):
        # Pushing to the back and popping from the front is a queue (FIFO)
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        dq.push_back(3)
        assert dq.pop_front() == 1
        assert dq.pop_front() == 2
        assert dq.pop_front() == 3


# ---------------------------------------------------------------------------
# pop_back
# ---------------------------------------------------------------------------

class TestPopBack:
    def test_pop_back_returns_last_element(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.pop_back() == 3

    def test_pop_back_removes_last_element(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert list(dq) == [1, 2]

    def test_pop_back_decreases_length(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert len(dq) == 2

    def test_pop_back_updates_peek_back(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert dq.peek_back() == 2

    def test_pop_back_does_not_change_peek_front(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert dq.peek_front() == 1

    def test_pop_back_single_element_empties_dequeue(self):
        dq = make_dequeue(1)
        dq.pop_back()
        assert len(dq) == 0

    def test_pop_back_single_element_peek_back_raises(self):
        # After popping the last element, peek_back must raise
        dq = make_dequeue(1)
        dq.pop_back()
        with pytest.raises(IndexError):
            dq.peek_back()

    def test_pop_back_single_element_peek_front_raises(self):
        # After popping the last element, peek_front must also raise
        dq = make_dequeue(1)
        dq.pop_back()
        with pytest.raises(IndexError):
            dq.peek_front()

    def test_pop_back_empty_raises(self):
        dq = Dequeue()
        with pytest.raises(IndexError):
            dq.pop_back()

    def test_pop_back_lifo_order(self):
        # Pushing to the back and popping from the back is a stack (LIFO)
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        dq.push_back(3)
        assert dq.pop_back() == 3
        assert dq.pop_back() == 2
        assert dq.pop_back() == 1


# ---------------------------------------------------------------------------
# peek_front
# ---------------------------------------------------------------------------

class TestPeekFront:
    def test_peek_front_returns_first_element(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.peek_front() == 1

    def test_peek_front_does_not_remove_element(self):
        dq = make_dequeue(1, 2, 3)
        dq.peek_front()
        assert len(dq) == 3

    def test_peek_front_same_value_on_repeated_calls(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.peek_front() == dq.peek_front()

    def test_peek_front_updates_after_push_front(self):
        dq = make_dequeue(2, 3)
        dq.push_front(1)
        assert dq.peek_front() == 1

    def test_peek_front_updates_after_pop_front(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_front()
        assert dq.peek_front() == 2

    def test_peek_front_empty_raises(self):
        dq = Dequeue()
        with pytest.raises(IndexError):
            dq.peek_front()


# ---------------------------------------------------------------------------
# peek_back
# ---------------------------------------------------------------------------

class TestPeekBack:
    def test_peek_back_returns_last_element(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.peek_back() == 3

    def test_peek_back_does_not_remove_element(self):
        dq = make_dequeue(1, 2, 3)
        dq.peek_back()
        assert len(dq) == 3

    def test_peek_back_same_value_on_repeated_calls(self):
        dq = make_dequeue(1, 2, 3)
        assert dq.peek_back() == dq.peek_back()

    def test_peek_back_updates_after_push_back(self):
        dq = make_dequeue(1, 2)
        dq.push_back(3)
        assert dq.peek_back() == 3

    def test_peek_back_updates_after_pop_back(self):
        dq = make_dequeue(1, 2, 3)
        dq.pop_back()
        assert dq.peek_back() == 2

    def test_peek_back_empty_raises(self):
        dq = Dequeue()
        with pytest.raises(IndexError):
            dq.peek_back()


# ---------------------------------------------------------------------------
# push/pop interleaved (dequeue-specific usage patterns)
# ---------------------------------------------------------------------------

class TestInterleaved:
    def test_used_as_queue_fifo(self):
        # push_back + pop_front = FIFO queue
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        dq.push_back(3)
        assert dq.pop_front() == 1
        assert dq.pop_front() == 2
        assert dq.pop_front() == 3

    def test_used_as_stack_lifo(self):
        # push_back + pop_back = LIFO stack
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        dq.push_back(3)
        assert dq.pop_back() == 3
        assert dq.pop_back() == 2
        assert dq.pop_back() == 1

    def test_push_front_pop_back_fifo(self):
        # push_front + pop_back is also FIFO, just mirrored
        dq = Dequeue()
        dq.push_front(1)
        dq.push_front(2)
        dq.push_front(3)
        assert dq.pop_back() == 1
        assert dq.pop_back() == 2
        assert dq.pop_back() == 3

    def test_mixed_push_and_pop(self):
        dq = Dequeue()
        dq.push_back(1)
        dq.push_front(0)
        dq.push_back(2)
        assert list(dq) == [0, 1, 2]
        assert dq.pop_front() == 0
        assert dq.pop_back() == 2
        assert list(dq) == [1]

    def test_alternating_push_pop(self):
        dq = Dequeue()
        dq.push_back(1)
        assert dq.pop_front() == 1
        dq.push_front(2)
        assert dq.pop_back() == 2
        assert len(dq) == 0

    def test_peek_consistent_with_push_pop(self):
        dq = Dequeue()
        dq.push_back(1)
        dq.push_back(2)
        assert dq.peek_front() == 1
        assert dq.peek_back() == 2
        dq.pop_front()
        assert dq.peek_front() == 2
        assert dq.peek_back() == 2