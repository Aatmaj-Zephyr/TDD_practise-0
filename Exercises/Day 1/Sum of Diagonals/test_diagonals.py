"""
TDD tests to check the code for the absolute difference between the sums of its diagonals.
"""


import pytest
from diagonals import diagonal_difference, is_a_square_matrix
from diagonals import is_first_diagonal, first_sum, is_second_diagonal, second_sum


def test_single_element():
    """
    The function `test_single_element` tests the `diagonal_difference` function with a single element
    input and asserts that the result is 0.
    """
    assert diagonal_difference([1]) == 0


def test_first_diagonal_for_two_by_two_matrix():
    """
    The function `test_first_diagonal_for_two_by_two_matrix` tests the `diagonal_difference`
    function for a 2x2 matrix and asserts that the result is 2. It tests first diagonal
    """
    matrix = [1, 0,
              0, 1]
    assert diagonal_difference(matrix) == 2


def test_square_matrix():
    """
    The function `test_square_matrix()` tests whether a given matrix is a square matrix.
    """
    matrix1 = [1, 0, 0]
    assert is_a_square_matrix(matrix1) is False
    matrix2 = [1, 0, 0, 0]
    assert is_a_square_matrix(matrix2) is True


def test_incorrect_input():
    """
    The function `test_incorrect_input` tests if an error is raised when a non-square matrix is passed
    to the `diagonal_difference` function.
    """
    with pytest.raises(ValueError) as error_info:
        diagonal_difference([1, 2, 3])

    assert str(error_info.value) == "input provided is not a square matrix"


def test_second_diagonal_for_two_by_two_matrix():
    """
    The function `test_second_diagonal_for_two_by_two_matrix` tests the `diagonal_difference` function
    for a 2x2 matrix for second diagonal.
    """
    matrix = [0, 1,
              1, 0]
    assert diagonal_difference(matrix) == 2


def test_two_by_two_identity_matrix():
    """
    The function `test_two_by_two_identity_matrix` tests the `diagonal_difference` function on a 2x2
    identity matrix.
    """
    matrix = [1, 1,
              1, 1]
    assert diagonal_difference(matrix) == 0


def test_two_by_two_any_matrix():
    """
    The function `test_two_by_two_any_matrix` tests the `diagonal_difference` function on a 2x2 matrix
    and asserts that the result is 5.
    """
    matrix = [-1, 3,
              0, -1]
    assert diagonal_difference(matrix) == 5


def test_first_diagonal_check():
    """
    The function `test_first_diagonal_check` tests the `is_first_diagonal` function by asserting that it
    returns the expected values for different input coordinates.
    """
    assert is_first_diagonal(0, 2) is True and is_first_diagonal(1, 3) is False


def test_second_diagonal_check():
    """
    The function `test_second_diagonal_check()` tests the correctness of the `is_second_diagonal()`
    function for different input coordinates.
    """
    assert is_second_diagonal(0, 3) is False and is_second_diagonal(
        1, 2) is True and is_second_diagonal(4, 3) is True


def test_first_sum():
    """
    The function `test_first_sum()` tests the `first_sum()` function by creating a matrix and asserting
    that the result of calling `first_sum(matrix)` is equal to the sum of its first diagonal.
    """
    matrix = [1, 0, 0,
              0, 1, 1,
              2, 0, 1]
    assert first_sum(matrix) == 3


def test_second_sum():
    """
    The test_second_sum function tests the second_sum function by creating a matrix and asserting that
    the result of calling second_sum on the matrix is equal to sum of second diagonal.
    """
    matrix = [1, 0, 1,
              0, 1, 1,
              2, 0, 1]
    assert second_sum(matrix) == 4


def test_three_by_three_matrix():
    """
    The test_three_by_three_matrix function tests the diagonal_difference function with a 3x3 matrix and
    asserts that the result is the absolute difference of the sum of its diagonals.
    """
    matrix = [1, 0, 0,
              0, 1, 1,
              2, 0, 1]
    assert diagonal_difference(matrix) == 0


def test_all():
    """
    The function `test_all` tests the `diagonal_difference` function by creating a matrix and asserting
    that the diagonal difference is equal to the absolute difference in the sum of diagonals.
    """
    matrix = [1, 2, 3,
              4, 5, 6,
              9, 8, 9,]
    assert diagonal_difference(matrix) == 2


def test_four_by_four_matrix():
    """
    The function `test_four_by_four_matrix` tests the required output on a 4x4 matrix.
    """
    matrix = [1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11, 12,
              13, 14, 15, 16]

    assert first_sum(matrix) == 34
    assert second_sum(matrix) == 34
    assert diagonal_difference(matrix) == 0
