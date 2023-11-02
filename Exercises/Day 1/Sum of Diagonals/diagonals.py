"""Code for absolute difference between the sums of its diagonals."""


def diagonal_difference(matrix: list[int]) -> int:
    """
    The function `diagonal_difference` calculates the absolute difference between the sum of the main
    diagonal and the sum of the secondary diagonal of a given matrix.

    :param matrix: The parameter `matrix` is a list of lists, where each inner list represents a row of
    the matrix. Each element in the inner list is an integer
    :type matrix: list[int]
    :return: The function `diagonal_difference` returns the absolute difference between the sum of the
    elements on the main diagonal and the sum of the elements on the secondary diagonal of the given
    matrix.
    """
    sum_of_diagonal = first_sum(matrix)
    sum_of_diagonal2 = second_sum(matrix)
    return abs(sum_of_diagonal - sum_of_diagonal2)


def first_sum(matrix: list[int]) -> int:
    """
    The function `first_sum` calculates the sum of elements in the first diagonal of a square matrix.

    :param matrix: The `matrix` parameter is a list of integers
    :type matrix: list[int]
    :return: the sum of the elements in the first diagonal of the matrix.
    """
    sum_first = 0
    order = len(matrix)**0.5
    for row_index, matrix_value in enumerate(matrix):
        if is_first_diagonal(row_index, order):
            sum_first += matrix_value
    return sum_first


def is_first_diagonal(i: int, order: int) -> bool:
    """
    The function checks if a given index belongs to the first diagonal of a square matrix.

    :param i: The index of the element in a 2D matrix
    :type i: int
    :param order: The order parameter represents the size of a square matrix. It indicates the number of
    rows or columns in the matrix
    :type order: int
    :return: a boolean value indicating whether the given index `i` is on the first diagonal of a square
    matrix of the given `order`.
    """

    return i % order == i//order


def second_sum(matrix: list[int]) -> int:
    """
    The function `second_sum` calculates the sum of values in the second diagonal of a square matrix.
    
    :param matrix: The parameter `matrix` is a list of integers
    :type matrix: list[int]
    :return: the sum of the values in the second diagonal of the matrix.
    """
    sum_second = 0
    order = len(matrix)**0.5
    for row_index, matrix_value in enumerate(matrix):
        if is_second_diagonal(row_index, order):
            sum_second += matrix_value
    return sum_second


def is_second_diagonal(i: int, order: int) -> bool:
    """
    The function `is_second_diagonal` checks if a given index `i` belongs to the second diagonal of a
    square matrix of order `order`.

    :param i: The parameter `i` represents the index of an element in a square matrix
    :type i: int
    :param order: The order parameter represents the size of a square matrix. It indicates the number of
    rows and columns in the matrix
    :type order: int
    :return: a boolean value indicating whether the given index `i` belongs to the second diagonal of a
    square matrix of the given `order`.
    """

    return i % order == order - i//order - 1
