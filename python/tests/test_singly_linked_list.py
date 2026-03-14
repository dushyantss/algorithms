import pytest
from data_structures.singly_linked_list import SinglyLinkedList


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_list(*values) -> SinglyLinkedList:
    """Convenience: create a SinglyLinkedList pre-populated with values."""
    sll = SinglyLinkedList()
    for v in values:
        sll.append(v)
    return sll


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        sll = SinglyLinkedList()
        assert len(sll) == 0


# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_append(self):
        sll = SinglyLinkedList()
        sll.append(1)
        assert len(sll) == 1

    def test_len_decreases_on_delete(self):
        sll = make_list(1, 2, 3)
        del sll[0]
        assert len(sll) == 2

    def test_len_after_multiple_appends(self):
        sll = SinglyLinkedList()
        for i in range(5):
            sll.append(i)
        assert len(sll) == 5


# ---------------------------------------------------------------------------
# __getitem__
# ---------------------------------------------------------------------------

class TestGetItem:
    def test_positive_index(self):
        sll = make_list(10, 20, 30)
        assert sll[0] == 10
        assert sll[1] == 20
        assert sll[2] == 30

    def test_negative_index(self):
        sll = make_list(10, 20, 30)
        assert sll[-1] == 30
        assert sll[-2] == 20
        assert sll[-3] == 10

    def test_out_of_bounds_positive_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            _ = sll[3]

    def test_out_of_bounds_negative_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            _ = sll[-4]

    def test_empty_list_raises(self):
        sll = SinglyLinkedList()
        with pytest.raises(IndexError):
            _ = sll[0]

    def test_slice_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            _ = sll[0:2]


# ---------------------------------------------------------------------------
# __setitem__
# ---------------------------------------------------------------------------

class TestSetItem:
    def test_positive_index(self):
        sll = make_list(1, 2, 3)
        sll[1] = 99
        assert sll[1] == 99

    def test_negative_index(self):
        sll = make_list(1, 2, 3)
        sll[-1] = 99
        assert sll[2] == 99

    def test_set_does_not_change_length(self):
        sll = make_list(1, 2, 3)
        sll[0] = 99
        assert len(sll) == 3

    def test_out_of_bounds_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            sll[5] = 99

    def test_out_of_bounds_negative_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            sll[-4] = 99

    def test_slice_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            sll[0:2] = [9, 9]


# ---------------------------------------------------------------------------
# __delitem__
# ---------------------------------------------------------------------------

class TestDelItem:
    def test_delete_first_element(self):
        sll = make_list(1, 2, 3)
        del sll[0]
        assert list(sll) == [2, 3]

    def test_delete_last_element(self):
        sll = make_list(1, 2, 3)
        del sll[2]
        assert list(sll) == [1, 2]

    def test_delete_middle_element(self):
        sll = make_list(1, 2, 3)
        del sll[1]
        assert list(sll) == [1, 3]

    def test_delete_with_negative_index(self):
        sll = make_list(1, 2, 3)
        del sll[-1]
        assert list(sll) == [1, 2]

    def test_delete_reduces_length(self):
        sll = make_list(1, 2, 3)
        del sll[0]
        assert len(sll) == 2

    def test_delete_relinks_nodes_correctly(self):
        sll = make_list(10, 20, 30, 40)
        del sll[1]
        # 20 is gone, 30 and 40 shift left
        assert sll[0] == 10
        assert sll[1] == 30
        assert sll[2] == 40

    def test_out_of_bounds_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(IndexError):
            del sll[5]

    def test_slice_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(NotImplementedError):
            del sll[0:2]


# ---------------------------------------------------------------------------
# insert
# ---------------------------------------------------------------------------

class TestInsert:
    def test_insert_at_beginning(self):
        sll = make_list(2, 3)
        sll.insert(0, 1)
        assert list(sll) == [1, 2, 3]

    def test_insert_at_middle(self):
        sll = make_list(1, 3)
        sll.insert(1, 2)
        assert list(sll) == [1, 2, 3]

    def test_insert_at_end(self):
        sll = make_list(1, 2)
        sll.insert(2, 3)
        assert list(sll) == [1, 2, 3]

    def test_insert_beyond_end_clamps_to_append(self):
        # Python's list.insert(999, x) appends rather than raising
        sll = make_list(1, 2, 3)
        sll.insert(999, 4)
        assert list(sll) == [1, 2, 3, 4]

    def test_insert_beyond_start_clamps_to_prepend(self):
        # Python's list.insert(-999, x) prepends rather than raising
        sll = make_list(1, 2, 3)
        sll.insert(-999, 0)
        assert list(sll) == [0, 1, 2, 3]

    def test_insert_negative_index(self):
        # insert(-1, x) inserts before the last element
        sll = make_list(1, 2, 4)
        sll.insert(-1, 3)
        assert list(sll) == [1, 2, 3, 4]

    def test_insert_increases_length(self):
        sll = make_list(1, 2, 3)
        sll.insert(0, 0)
        assert len(sll) == 4

    def test_insert_into_empty_list(self):
        sll = SinglyLinkedList()
        sll.insert(0, 42)
        assert list(sll) == [42]


# ---------------------------------------------------------------------------
# Mixin methods (provided free by MutableSequence)
# ---------------------------------------------------------------------------

class TestAppend:
    def test_append_adds_to_end(self):
        sll = SinglyLinkedList()
        sll.append(1)
        sll.append(2)
        assert sll[0] == 1
        assert sll[1] == 2

    def test_append_increases_length(self):
        sll = SinglyLinkedList()
        sll.append(42)
        assert len(sll) == 1

    def test_append_to_empty(self):
        sll = SinglyLinkedList()
        sll.append(1)
        assert list(sll) == [1]


class TestPop:
    def test_pop_returns_last_element(self):
        sll = make_list(1, 2, 3)
        assert sll.pop() == 3

    def test_pop_removes_last_element(self):
        sll = make_list(1, 2, 3)
        sll.pop()
        assert list(sll) == [1, 2]

    def test_pop_with_index(self):
        sll = make_list(1, 2, 3)
        assert sll.pop(0) == 1
        assert list(sll) == [2, 3]

    def test_pop_with_negative_index(self):
        sll = make_list(1, 2, 3)
        assert sll.pop(-2) == 2
        assert list(sll) == [1, 3]

    def test_pop_empty_raises(self):
        sll = SinglyLinkedList()
        with pytest.raises(IndexError):
            sll.pop()


class TestRemove:
    def test_remove_first_occurrence(self):
        sll = make_list(1, 2, 3, 2)
        sll.remove(2)
        assert list(sll) == [1, 3, 2]

    def test_remove_decreases_length(self):
        sll = make_list(1, 2, 3)
        sll.remove(2)
        assert len(sll) == 2

    def test_remove_not_found_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(ValueError):
            sll.remove(99)


class TestContains:
    def test_contains_present_value(self):
        sll = make_list(1, 2, 3)
        assert 2 in sll

    def test_contains_absent_value(self):
        sll = make_list(1, 2, 3)
        assert 99 not in sll

    def test_contains_empty(self):
        sll = SinglyLinkedList()
        assert 1 not in sll


class TestIter:
    def test_iter_yields_all_values_in_order(self):
        sll = make_list(10, 20, 30)
        assert list(sll) == [10, 20, 30]

    def test_iter_empty(self):
        sll = SinglyLinkedList()
        assert list(sll) == []


class TestReversed:
    def test_reversed_yields_values_in_reverse(self):
        sll = make_list(1, 2, 3)
        assert list(reversed(sll)) == [3, 2, 1]


class TestIndex:
    def test_index_returns_first_position(self):
        sll = make_list(10, 20, 30, 20)
        assert sll.index(20) == 1

    def test_index_not_found_raises(self):
        sll = make_list(1, 2, 3)
        with pytest.raises(ValueError):
            sll.index(99)


class TestCount:
    def test_count_multiple_occurrences(self):
        sll = make_list(1, 2, 2, 3, 2)
        assert sll.count(2) == 3

    def test_count_no_occurrences(self):
        sll = make_list(1, 2, 3)
        assert sll.count(99) == 0

    def test_count_single_occurrence(self):
        sll = make_list(1, 2, 3)
        assert sll.count(1) == 1


class TestExtend:
    def test_extend_adds_all_elements(self):
        sll = make_list(1, 2)
        sll.extend([3, 4, 5])
        assert list(sll) == [1, 2, 3, 4, 5]

    def test_extend_empty_iterable(self):
        sll = make_list(1, 2)
        sll.extend([])
        assert list(sll) == [1, 2]

    def test_extend_increases_length(self):
        sll = make_list(1, 2)
        sll.extend([3, 4])
        assert len(sll) == 4


class TestClear:
    def test_clear_empties_list(self):
        sll = make_list(1, 2, 3)
        sll.clear()
        assert len(sll) == 0

    def test_clear_makes_iter_empty(self):
        sll = make_list(1, 2, 3)
        sll.clear()
        assert list(sll) == []


class TestReverse:
    def test_reverse_in_place(self):
        sll = make_list(1, 2, 3)
        sll.reverse()
        assert list(sll) == [3, 2, 1]

    def test_reverse_single_element(self):
        sll = make_list(42)
        sll.reverse()
        assert list(sll) == [42]

    def test_reverse_empty(self):
        sll = SinglyLinkedList()
        sll.reverse()  # should not raise
        assert list(sll) == []