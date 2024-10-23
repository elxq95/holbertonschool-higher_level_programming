#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute
"""


class Square:
    """
    A class that defines a square by its size.
    Attributes:
    size: The size of the square (private attribute).
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size: The size of the square.
        """
        self.__size = size  # Private instance attribute
