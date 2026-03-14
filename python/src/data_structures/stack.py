class Stack:
    def __init__(self):
        self._array = []
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def push(self, value):
        self._array.append(value)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Stack is empty")

        self._size -= 1
        return self._array.pop()

    def peek(self):
        if self._size == 0:
            raise IndexError("Stack is empty")
        return self._array[-1]
