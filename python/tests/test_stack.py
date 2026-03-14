import pytest
from data_structures.stack import Stack


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        s = Stack()
        assert len(s) == 0


# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_push(self):
        s = Stack()
        s.push(1)
        assert len(s) == 1

    def test_len_decreases_on_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()
        assert len(s) == 1

    def test_len_after_multiple_pushes(self):
        s = Stack()
        for i in range(5):
            s.push(i)
        assert len(s) == 5


# ---------------------------------------------------------------------------
# push
# ---------------------------------------------------------------------------

class TestPush:
    def test_push_increases_length(self):
        s = Stack()
        s.push(42)
        assert len(s) == 1

    def test_push_multiple_increases_length(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert len(s) == 3

    def test_push_makes_value_accessible_via_peek(self):
        s = Stack()
        s.push(99)
        assert s.peek() == 99

    def test_push_updates_top(self):
        # The most recently pushed value should always be at the top
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2


# ---------------------------------------------------------------------------
# pop
# ---------------------------------------------------------------------------

class TestPop:
    def test_pop_returns_last_pushed_value(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2

    def test_pop_removes_top_element(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()
        assert s.peek() == 1

    def test_pop_decreases_length(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()
        assert len(s) == 1

    def test_pop_lifo_order(self):
        # Elements must come out in last-in-first-out order
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_pop_empties_stack(self):
        s = Stack()
        s.push(1)
        s.pop()
        assert len(s) == 0

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_pop_until_empty_then_raises(self):
        s = Stack()
        s.push(1)
        s.pop()
        with pytest.raises(IndexError):
            s.pop()


# ---------------------------------------------------------------------------
# peek
# ---------------------------------------------------------------------------

class TestPeek:
    def test_peek_returns_top_value(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2

    def test_peek_does_not_remove_element(self):
        s = Stack()
        s.push(1)
        s.peek()
        assert len(s) == 1

    def test_peek_same_value_on_repeated_calls(self):
        s = Stack()
        s.push(42)
        assert s.peek() == s.peek()

    def test_peek_updates_after_push(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1
        s.push(2)
        assert s.peek() == 2

    def test_peek_updates_after_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()
        assert s.peek() == 1

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()