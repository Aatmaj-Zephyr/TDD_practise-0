"""Document contains only one class - stack."""


class Stack:
    """ The `Stack` class is a data structure that allows for the addition and removal of elements in a
last-in, first-out (LIFO) manner. """

    def __init__(self) -> None:
        self.length = 0
        self.stack_memory_space: list[int] = []


    def get_length(self,) -> int:
        """
        The function `get_length` returns the length of an object.
        :return: The method `get_length` is returning the value of the attribute `length`.
        """
        return self.length

    def push(self, value: int) -> None:
        """
        The push function adds a value to the stack memory space and increments the length of the stack.

        :param value: The `value` parameter is an integer that represents the value to be pushed onto the
        stack
        :type value: int
        """
        self.stack_memory_space.append(value)
        self.length += 1

    def pop(self,) -> int:
        """
        The `pop` function removes and returns the top element from a stack, raising an error if the stack
        is empty.
        :return: The `pop` method is returning an integer value.
        """
        if self.length == 0:
            raise IndexError("Cannot pop from an empty stack")
        value: int = self.stack_memory_space[self.length - 1]
        self.length -= 1
        return value
