#!/usr/bin/python3
#!/usr/bin/python3
"""
This module defines a Square class.

The Square class provides:
    - Private instance attribute: size
    - Property getter and setter for size with validation
    - A public method to calculate the area of the square
    - A public method to print the square using the '#' character

Example usage:
    square = Square(4)
    print(square.size)  # Output: 4
    print(square.area())  # Output: 16
    square.my_print()  # Output: A 4x4 square made of '#' characters
"""

class Square:
    """
    A class that defines a square by its size and allows the calculation of
    the square's area as well as printing a visual representation of the square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size=0): Initializes the square with an optional size.
        size(self): Retrieves the size of the square.
        size(self, value): Sets the size of the square with validation.
        area(self): Returns the area of the square.
        my_print(self): Prints the square with '#' character or an empty line.
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
        self.size = size  # Uses the property setter for validation

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
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If the size of the square is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
