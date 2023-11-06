"""Testing for run length encoding"""

from run_length import rle, input_string_validate, make_list_of_continuouse_same_numbers
import pytest


def test_rle_for_one_number_one_time():
    """
    The function `test_rle_for_one_number_one_time` tests the `rle` function for encoding a single
    number occurring once.
    """
    assert rle("0") == "01"
    assert rle("2") == "21"


def test_rle_for_one_number_many_times():
    """
    The function `test_rle_for_one_number_many_times` tests the `rle` function for encoding a single
    number repeated multiple times.
    """
    assert rle("00") == "02"
    assert rle("222") == "23"


def test_rle_for_invalid_input():
    """
    The function `test_rle_for_invalid_input` tests the behavior of the `rle` function when it is called
    with invalid input.
    """
    with pytest.raises(ValueError) as error_info:
        rle("abc")
    assert error_info is not None


def test_correct_string_input_validate():
    """
    The function `test_correct_string_input_validate` tests the `input_string_validate` function with
    the input "123" and expects the result to be True.
    """
    assert input_string_validate("123") is True


def test_incorrect_string_input_validate():
    """
    The function `test_incorrect_string_input_validate` tests the `input_string_validate` function with
    incorrect string inputs.
    """
    assert input_string_validate("123a2") is False
    assert input_string_validate("abewf") is False


def test_many_inputs_many_times():
    """
    The function `test_many_inputs_many_times` tests the `rle` function with multiple inputs and checks
    if the output is as expected.
    """
    assert rle("1122") == "1222"
    assert rle("12234") == "11223141"
    assert rle("0000000011111111") == "0818"
    assert rle("000000001111111100") == "081802"


def test_unique_string_finder():
    """
    The function `test_unique_string_finder` tests the `unique_string_finder` function by asserting that
    it returns the expected output for a given input.
    """
    assert make_list_of_continuouse_same_numbers("1122") == ["11", "22"]
