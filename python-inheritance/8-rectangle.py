#!/usr/bin/python3
"""
This module provides a class called BaseGeometry and a subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherited from class Geometry
    """
    def __init__(self, width, height):
        """
        function that instantiates a rectangle instance

        Parameters:
        width: must be integer
        height: must be integer
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
