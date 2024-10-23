#!/usr/bin/python3
"""
This module provides a class called BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry

    >>> bg = BaseGeometry()
    >>> bg.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented
    """
    def area(self):
        """
        function that calculates area

        Parameters:
        self: the size

        Raises:
            Exception: Indicating that the area() method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that calculates area

        Parameters:
        self: the size
        name: name must be string
        value: value must be integer

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
