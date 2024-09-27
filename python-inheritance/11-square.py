#!/usr/bin/python3
"""
This module provides a class called BaseGeometry and a subclass Rectangle
"""


class BaseGeometry:
    """
    class BaseGeometry
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


class Rectangle(BaseGeometry):
    """
    class Rectangle inherited from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        function that instantiates a rectangle instance

        Parameters:
        self: the size
        width: mustr be integer
        height: must be integer
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        function that calculates area

        Parameters:
        self: the size

        Return:
        result of area formula
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        function that print the area formula

        Parameters:
        self: the size

        Return:
        full formula
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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

    def __str__(self):
        """
        function that print the area formula

        Parameters:
        self: the size

        Return:
        full formula
        """
        return f"[Square] {self.__size}/{self.__size}"
