#!/usr/bin/python3
"""
This module provides a function print_square(size)
that print a square of '#'
size has to be an integer or float
TypeError is raised if size is not integer type.
"""


def print_square(size):
    """
    Prints square of #

    Parameters:
    size: dimension of thesquare

    Returns:
    size: length of the square

    Raises:
    TypeError: the size must be an integer and not less than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for j in range(size):
        print('#' * size)
