"""The `Queue` class is a basic implementation of a queue data structure in Python, with methods to add
elements to the queue, remove elements from the queue, and get the length of the queue."""


class Queue:
    """Implementation of the Queue data structure.

    :Raises: IndexError: if the queue is empty and a remove operation is attempted

    :Returns:_type_: integer
    """

    length: int
    queue_memory: list[int]

    def __init__(self) -> None:
        self.length: int = 0
        self.queue_memory: list[int] = []

    def get_length(self,) -> int:
        """
        The function `get_length` returns the length of an object.
        :return: The method `get_length` is returning the value of the attribute `length`.
        """
        return self.length

    def add(self, value: int) -> None:
        """
        The add function increases the length of the queue by 1 and appends a value to the queue memory.

        :param value: The `value` parameter is an integer that represents the value to be added to the queue
        :type value: int
        """
        self.length += 1
        self.queue_memory.append(value)

    def remove(self,) -> int:
        """
        The `remove` function removes and returns the first element from a queue, raising an error if the
        queue is empty.
        
        :return: The value that is being removed from the queue is being returned.
        """
        if self.length <= 0:
            raise IndexError("Cannot remove from empty queue")
        value: int = self.queue_memory.pop(0)
        self.length -= 1

        return value
