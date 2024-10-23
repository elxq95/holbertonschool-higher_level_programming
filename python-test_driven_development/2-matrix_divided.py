#!/usr/bin/python3
"""
This module provides a function print_square(size)
that print a square of '#'
size has to be an integer or float
TypeError is raised if size is not integer type.
"""


def matrix_divided(matrix, div):
    """
    Prints divides all elements of a matrix

    Parameters:
    matrix (list of lists of numbers): The 2D matrix to be processed.
    div (number): The divisor. Must be non-zero.

    Returns:
    list of lists of floats: The new matrix with each element divided by div.

    Raises:
    TypeError: the matrix must be string or float type
    ZeroDivisionError: can't be divided by 0
    ValueError: If the rows of the matrix are not all the same size
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(
        isinstance(elem, (int, float))
        for row in matrix
        for elem in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size")
    for row in matrix:
        if len(row) != length:
            raise TypeError(
                "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    i = 0
    for i in matrix:
        new_matrix.append([round(j / div, 2) for j in i])
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
