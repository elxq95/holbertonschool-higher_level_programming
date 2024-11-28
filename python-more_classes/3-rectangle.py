#!/usr/bin/python3
"""This module handles a rectangle area calculation.
This module provides a function area()
that calculates the area of rectangle by using the length of one side
"""


class Rectangle:
    """A class represents a rectangle.
    Attributes
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.

    Methods
    -------
    __init__(width=0, height=0):
        initializes the rectangle with a given side length
    area():
        Return the area of the rectangle

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            print("")
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        # This condition checks if either the width or height of the rectangle is 0. 
        # If so, it returns an empty string (""), meaning that no visual representation is provided.
	•	This is logical because a rectangle with a width or height of 0 has no visible area, so it shouldn’t produce any output when printed.
        return '\n'.join([self.__width * '#'] * self.__height)
    # 	self.__width * '#': This creates a string of # characters equal to the width of the rectangle. 
    # For example, if self.__width is 4, it creates the string "####".