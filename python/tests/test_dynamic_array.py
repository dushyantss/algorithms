import pytest
from data_structures.dynamic_array import DynamicArray, INITIAL_CAPACITY  # INITIAL_CAPACITY used for growth test sizing only


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_array(*values) -> DynamicArray:
    """Convenience: create a DynamicArray pre-populated with values."""
    da = DynamicArray()
    for v in values:
        da.append(v)
    return da


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

class TestInit:
    def test_starts_empty(self):
        da = DynamicArray()
        assert len(da) == 0



# ---------------------------------------------------------------------------
# __len__
# ---------------------------------------------------------------------------

class TestLen:
    def test_len_increases_on_append(self):
        da = DynamicArray()
        da.append(1)
        assert len(da) == 1

    def test_len_decreases_on_delete(self):
        da = make_array(1, 2, 3)
        del da[0]
        assert len(da) == 2

    def test_len_after_multiple_appends(self):
        da = DynamicArray()
        for i in range(5):
            da.append(i)
        assert len(da) == 5


# ---------------------------------------------------------------------------
# __getitem__
# ---------------------------------------------------------------------------

class TestGetItem:
    def test_positive_index(self):
        da = make_array(10, 20, 30)
        assert da[0] == 10
        assert da[1] == 20
        assert da[2] == 30

    def test_negative_index(self):
        da = make_array(10, 20, 30)
        assert da[-1] == 30
        assert da[-2] == 20
        assert da[-3] == 10

    def test_out_of_bounds_positive_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(IndexError):
            _ = da[3]

    def test_out_of_bounds_negative_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(IndexError):
            _ = da[-4]

    def test_empty_array_raises(self):
        da = DynamicArray()
        with pytest.raises(IndexError):
            _ = da[0]


# ---------------------------------------------------------------------------
# __setitem__
# ---------------------------------------------------------------------------

class TestSetItem:
    def test_positive_index(self):
        da = make_array(1, 2, 3)
        da[1] = 99
        assert da[1] == 99

    def test_negative_index(self):
        da = make_array(1, 2, 3)
        da[-1] = 99
        assert da[2] == 99

    def test_set_does_not_change_length(self):
        da = make_array(1, 2, 3)
        da[0] = 99
        assert len(da) == 3

    def test_out_of_bounds_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(IndexError):
            da[5] = 99

    def test_out_of_bounds_negative_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(IndexError):
            da[-4] = 99


# ---------------------------------------------------------------------------
# __delitem__
# ---------------------------------------------------------------------------

class TestDelItem:
    def test_delete_first_element(self):
        da = make_array(1, 2, 3)
        del da[0]
        assert list(da) == [2, 3]

    def test_delete_last_element(self):
        da = make_array(1, 2, 3)
        del da[2]
        assert list(da) == [1, 2]

    def test_delete_middle_element(self):
        da = make_array(1, 2, 3)
        del da[1]
        assert list(da) == [1, 3]

    def test_delete_with_negative_index(self):
        da = make_array(1, 2, 3)
        del da[-1]
        assert list(da) == [1, 2]

    def test_delete_reduces_length(self):
        da = make_array(1, 2, 3)
        del da[0]
        assert len(da) == 2

    def test_delete_shifts_elements_correctly(self):
        da = make_array(10, 20, 30, 40)
        del da[1]
        # 20 is gone, 30 and 40 shift left
        assert da[0] == 10
        assert da[1] == 30
        assert da[2] == 40

    def test_out_of_bounds_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(IndexError):
            del da[5]


# ---------------------------------------------------------------------------
# insert
# ---------------------------------------------------------------------------

class TestInsert:
    def test_insert_at_beginning(self):
        da = make_array(2, 3)
        da.insert(0, 1)
        assert list(da) == [1, 2, 3]

    def test_insert_at_middle(self):
        da = make_array(1, 3)
        da.insert(1, 2)
        assert list(da) == [1, 2, 3]

    def test_insert_at_end(self):
        da = make_array(1, 2)
        da.insert(2, 3)
        assert list(da) == [1, 2, 3]

    def test_insert_beyond_end_clamps_to_append(self):
        # Python's list.insert(999, x) appends rather than raising
        da = make_array(1, 2, 3)
        da.insert(999, 4)
        assert list(da) == [1, 2, 3, 4]

    def test_insert_beyond_start_clamps_to_prepend(self):
        # Python's list.insert(-999, x) prepends rather than raising
        da = make_array(1, 2, 3)
        da.insert(-999, 0)
        assert list(da) == [0, 1, 2, 3]

    def test_insert_negative_index(self):
        # insert(-1, x) inserts before the last element
        da = make_array(1, 2, 4)
        da.insert(-1, 3)
        assert list(da) == [1, 2, 3, 4]

    def test_insert_increases_length(self):
        da = make_array(1, 2, 3)
        da.insert(0, 0)
        assert len(da) == 4


# ---------------------------------------------------------------------------
# Growth (capacity doubling)
# ---------------------------------------------------------------------------

class TestGrowth:
    def test_values_preserved_after_growth(self):
        # Insert one more element than the initial capacity to trigger growth
        da = DynamicArray()
        values = list(range(INITIAL_CAPACITY + 1))
        for v in values:
            da.append(v)
        assert list(da) == values

    def test_multiple_growths(self):
        da = DynamicArray()
        # Trigger several growth cycles
        n = INITIAL_CAPACITY * 4 + 1
        for i in range(n):
            da.append(i)
        assert len(da) == n
        assert list(da) == list(range(n))


# ---------------------------------------------------------------------------
# Mixin methods (provided free by MutableSequence)
# ---------------------------------------------------------------------------

class TestAppend:
    def test_append_adds_to_end(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        assert da[0] == 1
        assert da[1] == 2

    def test_append_increases_length(self):
        da = DynamicArray()
        da.append(42)
        assert len(da) == 1


class TestPop:
    def test_pop_returns_last_element(self):
        da = make_array(1, 2, 3)
        assert da.pop() == 3

    def test_pop_removes_last_element(self):
        da = make_array(1, 2, 3)
        da.pop()
        assert list(da) == [1, 2]

    def test_pop_with_index(self):
        da = make_array(1, 2, 3)
        assert da.pop(0) == 1
        assert list(da) == [2, 3]

    def test_pop_with_negative_index(self):
        da = make_array(1, 2, 3)
        assert da.pop(-2) == 2
        assert list(da) == [1, 3]

    def test_pop_empty_raises(self):
        da = DynamicArray()
        with pytest.raises(IndexError):
            da.pop()


class TestRemove:
    def test_remove_first_occurrence(self):
        da = make_array(1, 2, 3, 2)
        da.remove(2)
        assert list(da) == [1, 3, 2]

    def test_remove_decreases_length(self):
        da = make_array(1, 2, 3)
        da.remove(2)
        assert len(da) == 2

    def test_remove_not_found_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(ValueError):
            da.remove(99)


class TestContains:
    def test_contains_present_value(self):
        da = make_array(1, 2, 3)
        assert 2 in da

    def test_contains_absent_value(self):
        da = make_array(1, 2, 3)
        assert 99 not in da

    def test_contains_empty(self):
        da = DynamicArray()
        assert 1 not in da


class TestIter:
    def test_iter_yields_all_values_in_order(self):
        da = make_array(10, 20, 30)
        assert list(da) == [10, 20, 30]

    def test_iter_empty(self):
        da = DynamicArray()
        assert list(da) == []


class TestReversed:
    def test_reversed_yields_values_in_reverse(self):
        da = make_array(1, 2, 3)
        assert list(reversed(da)) == [3, 2, 1]


class TestIndex:
    def test_index_returns_first_position(self):
        da = make_array(10, 20, 30, 20)
        assert da.index(20) == 1

    def test_index_not_found_raises(self):
        da = make_array(1, 2, 3)
        with pytest.raises(ValueError):
            da.index(99)


class TestCount:
    def test_count_multiple_occurrences(self):
        da = make_array(1, 2, 2, 3, 2)
        assert da.count(2) == 3

    def test_count_no_occurrences(self):
        da = make_array(1, 2, 3)
        assert da.count(99) == 0

    def test_count_single_occurrence(self):
        da = make_array(1, 2, 3)
        assert da.count(1) == 1


class TestExtend:
    def test_extend_adds_all_elements(self):
        da = make_array(1, 2)
        da.extend([3, 4, 5])
        assert list(da) == [1, 2, 3, 4, 5]

    def test_extend_empty_iterable(self):
        da = make_array(1, 2)
        da.extend([])
        assert list(da) == [1, 2]

    def test_extend_increases_length(self):
        da = make_array(1, 2)
        da.extend([3, 4])
        assert len(da) == 4


class TestClear:
    def test_clear_empties_array(self):
        da = make_array(1, 2, 3)
        da.clear()
        assert len(da) == 0

    def test_clear_makes_iter_empty(self):
        da = make_array(1, 2, 3)
        da.clear()
        assert list(da) == []


class TestReverse:
    def test_reverse_in_place(self):
        da = make_array(1, 2, 3)
        da.reverse()
        assert list(da) == [3, 2, 1]

    def test_reverse_single_element(self):
        da = make_array(42)
        da.reverse()
        assert list(da) == [42]

    def test_reverse_empty(self):
        da = DynamicArray()
        da.reverse()  # should not raise
        assert list(da) == []