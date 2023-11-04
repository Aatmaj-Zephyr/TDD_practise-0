"""
Tests for queue using TDD
"""

from tdd_queue import Queue
import pytest


@pytest.fixture(name="my_queue")
def fixture_my_queue():
    """
    The function `fixture_my_queue()` returns a new instance of the `Queue` class.
    :return: The function `fixture_my_queue` is returning an instance of the `Queue` class.
    """
    return Queue()

def test_queue_creation(my_queue):
    """
    The function `test_queue` tests the `Queue` class by creating a queue and asserting that the length
    of the queue is 0.
    """

    assert my_queue.get_length() == 0


def test_add_to_queue_increases_length(my_queue):
    """
    The function tests whether adding elements to a queue increases its length.
    """

    original_length: int = my_queue.get_length()
    for _ in range(5):
        my_queue.add(1)
    new_length: int = my_queue.get_length()
    assert my_queue.get_length() == new_length - original_length


def test_remove_decreases_length(my_queue):
    """
    The function tests whether removing elements from a queue decreases its length to zero.
    """

    for _ in range(3):
        my_queue.add(2)
    for _ in range(3):
        my_queue.remove()

    assert my_queue.get_length() == 0


def test_cannot_remove_from_empty_queue(my_queue):
    """
    The function tests whether removing elements from an empty queue raises an error.
    """

    with pytest.raises(IndexError):
        my_queue.remove()


def test_putting_and_removing(my_queue):
    """
    The function tests putting and removing elements from a queue in a first-in-first-out (FIFO) order.
    """

    my_queue.add(1)
    my_queue.add(2)
    # FIFO
    assert my_queue.remove() == 1
    assert my_queue.remove() == 2
