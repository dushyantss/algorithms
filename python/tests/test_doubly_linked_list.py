import pytest
from data_structures.doubly_linked_list import SinglyLinkedList as DoublyLinkedList


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_list(*values) -> DoublyLinkedList:
    """Convenience: create a DoublyLinkedList pre-populated with values."""
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    return dll


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        dll = DoublyLinkedList()
        assert len(dll) == 0


# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_append(self):
        dll = DoublyLinkedList()
        dll.append(1)
        assert len(dll) == 1

    def test_len_decreases_on_delete(self):
        dll = make_list(1, 2, 3)
        del dll[0]
        assert len(dll) == 2

    def test_len_after_multiple_appends(self):
        dll = DoublyLinkedList()
        for i in range(5):
            dll.append(i)
        assert len(dll) == 5


# ---------------------------------------------------------------------------
# __getitem__
# ---------------------------------------------------------------------------

class TestGetItem:
    def test_positive_index(self):
        dll = make_list(10, 20, 30)
        assert dll[0] == 10
        assert dll[1] == 20
        assert dll[2] == 30

    def test_negative_index(self):
        dll = make_list(10, 20, 30)
        assert dll[-1] == 30
        assert dll[-2] == 20
        assert dll[-3] == 10

    def test_out_of_bounds_positive_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            _ = dll[3]

    def test_out_of_bounds_negative_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            _ = dll[-4]

    def test_empty_list_raises(self):
        dll = DoublyLinkedList()
        with pytest.raises(IndexError):
            _ = dll[0]

    def test_slice_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            _ = dll[0:2]


# ---------------------------------------------------------------------------
# __setitem__
# ---------------------------------------------------------------------------

class TestSetItem:
    def test_positive_index(self):
        dll = make_list(1, 2, 3)
        dll[1] = 99
        assert dll[1] == 99

    def test_negative_index(self):
        dll = make_list(1, 2, 3)
        dll[-1] = 99
        assert dll[2] == 99

    def test_set_does_not_change_length(self):
        dll = make_list(1, 2, 3)
        dll[0] = 99
        assert len(dll) == 3

    def test_out_of_bounds_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            dll[5] = 99

    def test_out_of_bounds_negative_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            dll[-4] = 99

    def test_slice_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            dll[0:2] = [9, 9]


# ---------------------------------------------------------------------------
# __delitem__
# ---------------------------------------------------------------------------

class TestDelItem:
    def test_delete_first_element(self):
        dll = make_list(1, 2, 3)
        del dll[0]
        assert list(dll) == [2, 3]

    def test_delete_last_element(self):
        dll = make_list(1, 2, 3)
        del dll[2]
        assert list(dll) == [1, 2]

    def test_delete_middle_element(self):
        dll = make_list(1, 2, 3)
        del dll[1]
        assert list(dll) == [1, 3]

    def test_delete_with_negative_index(self):
        dll = make_list(1, 2, 3)
        del dll[-1]
        assert list(dll) == [1, 2]

    def test_delete_reduces_length(self):
        dll = make_list(1, 2, 3)
        del dll[0]
        assert len(dll) == 2

    def test_delete_relinks_nodes_correctly(self):
        dll = make_list(10, 20, 30, 40)
        del dll[1]
        assert dll[0] == 10
        assert dll[1] == 30
        assert dll[2] == 40

    def test_delete_updates_tail(self):
        # Verify the tail pointer is correct after deleting the last element
        dll = make_list(1, 2, 3)
        del dll[2]
        # If tail is wrong, reversed iteration will break
        assert list(reversed(dll)) == [2, 1]

    def test_delete_updates_head(self):
        # Verify the head pointer is correct after deleting the first element
        dll = make_list(1, 2, 3)
        del dll[0]
        assert list(dll) == [2, 3]

    def test_out_of_bounds_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            del dll[5]

    def test_slice_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            del dll[0:2]


# ---------------------------------------------------------------------------
# insert
# ---------------------------------------------------------------------------

class TestInsert:
    def test_insert_at_beginning(self):
        dll = make_list(2, 3)
        dll.insert(0, 1)
        assert list(dll) == [1, 2, 3]

    def test_insert_at_middle(self):
        dll = make_list(1, 3)
        dll.insert(1, 2)
        assert list(dll) == [1, 2, 3]

    def test_insert_at_end(self):
        dll = make_list(1, 2)
        dll.insert(2, 3)
        assert list(dll) == [1, 2, 3]

    def test_insert_beyond_end_clamps_to_append(self):
        # Python's list.insert(999, x) appends rather than raising
        dll = make_list(1, 2, 3)
        dll.insert(999, 4)
        assert list(dll) == [1, 2, 3, 4]

    def test_insert_beyond_start_clamps_to_prepend(self):
        # Python's list.insert(-999, x) prepends rather than raising
        dll = make_list(1, 2, 3)
        dll.insert(-999, 0)
        assert list(dll) == [0, 1, 2, 3]

    def test_insert_negative_index(self):
        # insert(-1, x) inserts before the last element
        dll = make_list(1, 2, 4)
        dll.insert(-1, 3)
        assert list(dll) == [1, 2, 3, 4]

    def test_insert_increases_length(self):
        dll = make_list(1, 2, 3)
        dll.insert(0, 0)
        assert len(dll) == 4

    def test_insert_into_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert(0, 42)
        assert list(dll) == [42]

    def test_insert_updates_prev_links(self):
        # After inserting, reversed iteration must still be correct
        dll = make_list(1, 3)
        dll.insert(1, 2)
        assert list(reversed(dll)) == [3, 2, 1]

    def test_insert_at_beginning_updates_prev_links(self):
        dll = make_list(2, 3)
        dll.insert(0, 1)
        assert list(reversed(dll)) == [3, 2, 1]

    def test_insert_at_end_updates_tail(self):
        dll = make_list(1, 2)
        dll.insert(2, 3)
        assert list(reversed(dll)) == [3, 2, 1]


# ---------------------------------------------------------------------------
# __reversed__ (doubly linked list specific — uses prev pointers directly)
# ---------------------------------------------------------------------------

class TestReversed:
    def test_reversed_yields_values_in_reverse(self):
        dll = make_list(1, 2, 3)
        assert list(reversed(dll)) == [3, 2, 1]

    def test_reversed_single_element(self):
        dll = make_list(42)
        assert list(reversed(dll)) == [42]

    def test_reversed_empty(self):
        dll = DoublyLinkedList()
        assert list(reversed(dll)) == []

    def test_reversed_matches_forward_iteration_reversed(self):
        dll = make_list(1, 2, 3, 4, 5)
        assert list(reversed(dll)) == list(dll)[::-1]


# ---------------------------------------------------------------------------
# Mixin methods (provided free by MutableSequence)
# ---------------------------------------------------------------------------

class TestAppend:
    def test_append_adds_to_end(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        assert dll[0] == 1
        assert dll[1] == 2

    def test_append_increases_length(self):
        dll = DoublyLinkedList()
        dll.append(42)
        assert len(dll) == 1

    def test_append_to_empty(self):
        dll = DoublyLinkedList()
        dll.append(1)
        assert list(dll) == [1]

    def test_append_updates_tail(self):
        # Tail must be updated so reversed() works correctly after appending
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        assert list(reversed(dll)) == [3, 2, 1]


class TestPop:
    def test_pop_returns_last_element(self):
        dll = make_list(1, 2, 3)
        assert dll.pop() == 3

    def test_pop_removes_last_element(self):
        dll = make_list(1, 2, 3)
        dll.pop()
        assert list(dll) == [1, 2]

    def test_pop_with_index(self):
        dll = make_list(1, 2, 3)
        assert dll.pop(0) == 1
        assert list(dll) == [2, 3]

    def test_pop_with_negative_index(self):
        dll = make_list(1, 2, 3)
        assert dll.pop(-2) == 2
        assert list(dll) == [1, 3]

    def test_pop_empty_raises(self):
        dll = DoublyLinkedList()
        with pytest.raises(IndexError):
            dll.pop()


class TestRemove:
    def test_remove_first_occurrence(self):
        dll = make_list(1, 2, 3, 2)
        dll.remove(2)
        assert list(dll) == [1, 3, 2]

    def test_remove_decreases_length(self):
        dll = make_list(1, 2, 3)
        dll.remove(2)
        assert len(dll) == 2

    def test_remove_not_found_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(ValueError):
            dll.remove(99)


class TestContains:
    def test_contains_present_value(self):
        dll = make_list(1, 2, 3)
        assert 2 in dll

    def test_contains_absent_value(self):
        dll = make_list(1, 2, 3)
        assert 99 not in dll

    def test_contains_empty(self):
        dll = DoublyLinkedList()
        assert 1 not in dll


class TestIter:
    def test_iter_yields_all_values_in_order(self):
        dll = make_list(10, 20, 30)
        assert list(dll) == [10, 20, 30]

    def test_iter_empty(self):
        dll = DoublyLinkedList()
        assert list(dll) == []


class TestIndex:
    def test_index_returns_first_position(self):
        dll = make_list(10, 20, 30, 20)
        assert dll.index(20) == 1

    def test_index_not_found_raises(self):
        dll = make_list(1, 2, 3)
        with pytest.raises(ValueError):
            dll.index(99)


class TestCount:
    def test_count_multiple_occurrences(self):
        dll = make_list(1, 2, 2, 3, 2)
        assert dll.count(2) == 3

    def test_count_no_occurrences(self):
        dll = make_list(1, 2, 3)
        assert dll.count(99) == 0

    def test_count_single_occurrence(self):
        dll = make_list(1, 2, 3)
        assert dll.count(1) == 1


class TestExtend:
    def test_extend_adds_all_elements(self):
        dll = make_list(1, 2)
        dll.extend([3, 4, 5])
        assert list(dll) == [1, 2, 3, 4, 5]

    def test_extend_empty_iterable(self):
        dll = make_list(1, 2)
        dll.extend([])
        assert list(dll) == [1, 2]

    def test_extend_increases_length(self):
        dll = make_list(1, 2)
        dll.extend([3, 4])
        assert len(dll) == 4


class TestClear:
    def test_clear_empties_list(self):
        dll = make_list(1, 2, 3)
        dll.clear()
        assert len(dll) == 0

    def test_clear_makes_iter_empty(self):
        dll = make_list(1, 2, 3)
        dll.clear()
        assert list(dll) == []


class TestReverseInPlace:
    def test_reverse_in_place(self):
        dll = make_list(1, 2, 3)
        dll.reverse()
        assert list(dll) == [3, 2, 1]

    def test_reverse_single_element(self):
        dll = make_list(42)
        dll.reverse()
        assert list(dll) == [42]

    def test_reverse_empty(self):
        dll = DoublyLinkedList()
        dll.reverse()  # should not raise
        assert list(dll) == []