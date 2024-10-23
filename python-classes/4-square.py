#!/usr/bin/python3
"""
This module defines a Square class.

The Square class provides:
    - Private instance attribute: size
    - Property getter and setter for size with validation
    - A public method to calculate the area of the square

Example usage:
    square = Square(4)
    print(square.size)  # Output: 4
    print(square.area())  # Output: 16
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size=0): Initializes the square with an optional size.
        area(self): Returns the area of the square.
        size(self): Retrieves the size of the square.
        size(self, value): Sets the size of the square with validation.
    """
    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # This uses the property setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square, with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
