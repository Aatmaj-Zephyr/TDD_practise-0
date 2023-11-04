"""
Testing a stack
"""
import pytest
from stack import Stack




def test_stack_creation():
    """
    The function tests the creation of a stack object and asserts that it is not None.
    """
    # Create a new stack
    my_stack: Stack = Stack()

    # Assert that the stack is not None
    assert my_stack is not None


def test_stack_length():
    # Create a new stack

    """
    The function `test_stack_length` checks if the length of the stack is 0.
    """

    my_stack: Stack = Stack()
    assert my_stack.get_length() == 0


def test_push_increases_length():
    """
    The function tests whether pushing elements into a stack increases its length.
    """
    # Create a new stack
    my_stack: Stack = Stack()
    initial_length = my_stack.get_length()
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.get_length() - initial_length == 2


def test_pop_decreases_length():
    """
    The function tests whether the length of a stack decreases by 1 after calling the pop() method.
    """
    # Create a new stack
    my_stack: Stack = Stack()
    my_stack.push(1)
    initial_length = my_stack.get_length()
    my_stack.pop()
    assert my_stack.get_length() - initial_length == -1


def test_pop_returns_last_pushed_value():
    """
    The function tests if the pop method of a stack returns the last pushed value.
    """
    # Create a new stack
    my_stack: Stack = Stack()
    value = 10
    my_stack.push(value)
    returned_value: int = my_stack.pop()
    assert returned_value == value


def test_pop_returns_error_for_popping_on_empty_stack():
    """
    The function tests that popping from an empty stack raises an IndexError with the message "Cannot
    pop from an empty stack".
    """
    # Create a new stack
    my_stack: Stack = Stack()
    with pytest.raises(IndexError) as exc_info:
        my_stack.pop()

    assert str(exc_info.value) == "Cannot pop from an empty stack"


def test_last_first_out():
    """
    The function `test_last_first_out` tests the behavior of a stack by pushing two elements onto it,
    popping them off in reverse order, and asserting that the first popped element is the second element
    pushed and the last popped element is the first element pushed.
    """
    # Create a new stack
    my_stack: Stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    first: int = my_stack.pop()
    last: int = my_stack.pop()
    assert first == 2 and last == 1
