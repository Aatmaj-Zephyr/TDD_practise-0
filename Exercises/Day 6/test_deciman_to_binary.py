"""Code to test the conversion from decimal to binary"""
from decimal_to_binary import to_binary
import pytest
def test_zero():
    """
    The function `test_zero` tests if the `to_binary` function returns 0 when given 0 as input.
    """
    assert to_binary(0) == 0

def test_negative_number_returns_error():
    """
    The function `test_negative_number_returns_error` tests whether the `to_binary` function raises a
    `ValueError` when given a negative number as input.
    """
    with pytest.raises(ValueError) as error_info:
        to_binary(-1)
    assert error_info is not None

def test_one():
    """
    The function `test_one` tests the `to_binary` function by asserting that the output of
    `to_binary(1)` is equal to 1.
    """
    assert to_binary(1) == 1


def test_nums_that_return_two_digit_outputs():
    """
    The function `test_nums_that_return_two_digit_outputs` tests the `to_binary` function for numbers
    that return two-digit binary outputs.
    """
    assert to_binary(2) == 10
    assert to_binary(3) == 11

def test_nums_that_return_three_digit_outputs():
    """
    The function `test_nums_that_return_three_digit_outputs` tests the `to_binary` function for three
    different inputs and asserts that the outputs are three-digit binary numbers.
    """
    assert to_binary(4) == 100
    assert to_binary(5) == 101
    assert to_binary(6) == 110

def test_nums_that_return_four_digit_outputs():
    """
    The function `test_nums_that_return_four_digit_outputs` tests the `to_binary` function for numbers
    that result in four-digit binary outputs.
    """
    assert to_binary(8) == 1000
    assert to_binary(9) == 1001
    