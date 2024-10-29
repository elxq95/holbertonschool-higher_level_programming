#!/usr/bin/python3

"""
This module defines a Rectangle class with private instance attributes
for width and height, along with property methods for accessing and
setting these attributes with validation.
"""

class Rectangle:
    """A class that defines a rectangle by width and height."""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        """__init__ is the constructor method called automatically when a new instance of Rectangle is created.
	- self represents the instance of the class being created.
	- width and height are optional parameters with default values of 0. If you create a Rectangle without providing these values, they will automatically be set to 0."""
        
    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value