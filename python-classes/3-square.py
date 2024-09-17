#!/usr/bin/python3
"""
Module 4-square
Defines a class square with a private instance attribute"""


class Square:
    """
    A class that defines a square by its size
    Attributes:
    the size of the square (private attribute)"""
    def __init__(self, size=0):
        """
        initializes a new square instance
        Args:
            size (int): The size of the square (default is 0).
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        Returns:
        int: the area of the square.
        """
        return self.__size ** 2