#!/usr/bin/python3
"""
This module provides a function add_integer(a, b=98) that adds two integers.
If a or b are floats, they will be casted into integers before the addition.
TypeError is raised if a or b are not integer or float type.
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Parameters:
    a: int or float - the first number
    b: int or float, optional number - if none, default is 98

    Returns:
    int: The additions of two integers

    Raises:
    TypeError: If a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)