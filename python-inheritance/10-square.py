#!/usr/bin/python3
"""
This module provides a class called BaseGeometry and a subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inherited from class Rectangle
    """
    def __init__(self, size):
        """
        function that instantiates a square instance

        Parameters:
        self: the object
        sizet: must be integer
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        function that calculates area

        Parameters:
        self: the size

        Return:
        result of area formula
        """
        return (self.__size * self.__size)
