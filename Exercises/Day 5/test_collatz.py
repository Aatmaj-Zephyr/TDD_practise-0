"""Testing of collatz conjecture code"""

import pytest
from collatz import collatz


def test_negative_and_zero_input():
    """
    The function `test_negative_and_zero_input` tests whether the `collatz` function raises a
    `ValueError` when given negative or zero input.
    """
    with pytest.raises(ValueError) as error_info:
        collatz(-2)
        collatz(0)
    assert error_info is not None


def test_even():
    """
    The function `test_even` tests the `collatz` function for even numbers.
    """

    assert collatz(2) == 1
    assert collatz(4) == 2


def test_odd():
    """
    The test_odd function tests the collatz function with odd numbers and checks if the output is as
    expected.
    """
    assert collatz(3) == 10
    assert collatz(5) == 16
    assert collatz(1) == 4


def test_function_calling_multiple_times():
    """
    The function `test_function_calling_multiple_times` tests the `collatz` function by calling it
    multiple times with different inputs and checking the expected outputs.
    """
    first_call = collatz(7)
    assert first_call == 22
    second_call = collatz(first_call)
    assert second_call == 11
    third_call = collatz(second_call)
    assert third_call == 34


@pytest.mark.timeout(5)
def test_always_ends_in_one():
    """
    The function `test_always_ends_in_one` tests whether the `collatz` function always ends with the
    number 1 or goes into infinite loop.
    """
    test_number = 12312323

    while True:
        test_number = collatz(test_number)
        if test_number == 1:
            break
