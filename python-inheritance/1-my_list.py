#!/usr/bin/python3
"""
This module provides a function that returns
the list of sorted integers
"""


class MyList(list):
    """
    Custom list class that can print itself sorted.

    Parameters:
    self: the list of integers

    Returns:
    None
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
