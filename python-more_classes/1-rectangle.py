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

    def __init__(self, width=0, height=0): #init method initializes the rectangle's dimensions
        self.width = width # Think of self as a placeholder for “this object right here.”
        self.height = height #constructor
        # Purpose: This constructor allows an object of Rectangle to be 
        # created with specific width and height values.
# The width and height properties define controlled access to the rectangle’s dimensions, 
# enforcing specific rules using getter and setter methods.

    @property #getter -defines a getter for width and height, 
    # allowing them to be accessed as attributes (e.g., rect.width) 
    # rather than needing to call methods.
    # A getter is a method used to retrieve the value of an attribute from an object.

    def width(self):
        return self.__width

    @width.setter #This decorator defines a setter for width. It allows validation when setting a new width value:
    def width(self, value):
        # A setter is a method used to modify or set the value of an attribute in a controlled way.
        # self refers to the current instance of the class, 
        # and value is the new value that someone wants to set for width.
        # allow us to validate or modify the value before actually updating the attribute
        if not isinstance(value, int):
            # isinstance(value, int) returns True if value is an integer, and False otherwise.
            raise TypeError("width must be an integer")
        # If value is not an integer, the raise TypeError(...) line triggers an error, 
        # stopping the method and signaling that only integer values are allowed.
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        # Purpose: This line sets the private attribute self.__width to the validated value.
        # The __ before width (double underscores) is a Python convention to mark this attribute as “private.” 
        # This means it’s intended to be used only inside the class itself. Outside the class, you wouldn’t 
        # normally access __width directly; instead, 
        # you’d use methods provided by the class (like get_width or set_width) to access or modify it. 
        # This is a way of protecting the data and ensuring it’s handled properly.

    @property
    def height(self):
        return self.__height

    @height.setter
    # A setter is a method used to modify or set the value of an attribute in a controlled way.
        # self refers to the current instance of the class, 
        # and value is the new value that someone wants to set for width.
        # allow us to validate or modify the value before actually updating the attribute
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value #private attribute of the object
        # Attributes are like “data containers” that store information inside an object. 
        # Here, __height is meant to store the height of the rectangle.