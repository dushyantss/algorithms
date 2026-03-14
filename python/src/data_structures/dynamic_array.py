from collections.abc import MutableSequence

GROWTH_FACTOR = 2
INITIAL_CAPACITY = 8


class DynamicArray(MutableSequence):
    def __init__(self):
        self._array = [None] * INITIAL_CAPACITY
        self._size: int = 0
        self._capacity: int = len(self._array)

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int | slice):
        if isinstance(index, slice):
            return self._array[index]

        index = self._validated_index(index)
        return self._array[index]

    def __setitem__(self, index: int | slice, value):
        if isinstance(index, slice):
            self._array[index] = value
            self._size = len(self._array)
            self.capacity = len(self._array)
            return

        index = self._validated_index(index)
        self._array[index] = value

    def __delitem__(self, index: int | slice):
        if isinstance(index, slice):
            del self._array[index]
            self._size = len(self._array)
            self.capacity = len(self._array)
            return

        index = self._validated_index(index)
        value = self[index]

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._array[self._size - 1] = None
        self._size -= 1

        return value

    def insert(self, index: int, value):
        if index < 0:
            index += self._size

        if index <= 0:
            index = 0
        if index >= self._size:
            index = self._size

        if self._size < self._capacity:
            for i in range(self._size - 1, index - 1, -1):
                self._array[i + 1] = self._array[i]
            self._array[index] = value
            self._size += 1
        else:
            new_capacity = self._capacity * GROWTH_FACTOR
            new_array = [None] * new_capacity
            for i in range(index):
                new_array[i] = self._array[i]
            new_array[index] = value
            for i in range(index, self._size):
                new_array[i + 1] = self._array[i]

            self._array = new_array
            self._capacity = new_capacity
            self._size += 1

    ############### private methods ###############

    def _validated_index(self, index: int):
        if index < 0:
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        return index
