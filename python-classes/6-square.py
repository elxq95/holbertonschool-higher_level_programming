#!/usr/bin/python3
"""
This module defines a Square class.

The Square class provides:
    - Private instance attributes: size and position
    - Property getters and setters for size and position with validation
    - A public method to calculate the area of the square
    - A public method to print the square using the '#' character with space for position
"""


class Square:
    """
    A class that defines a square by its size and position, and allows the
    calculation of the square's area as well as printing a visual
    representation of the square considering position.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes the square with
        an optional size and position.
        size(self): Retrieves the size of the square.
        size(self, value): Sets the size of the square with validation.
        position(self): Retrieves the position of the square.
        position(self, value): Sets the position of the square with validation.
        area(self): Returns the area of the square.
        my_print(self): Prints the square with '#' character considering
        position.
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with an optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square, with validation.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character considering the position.

        If the size is 0, print an empty line. Print spaces based on the
        position before the '#' characters if position[1] > 0.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
