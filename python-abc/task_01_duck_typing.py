#!/usr/bin/python3
"""
This module provides a function that returns
the area of each shape
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    class Shape inherited from ABC class
    """
    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by all subclasses.
        Each shape should return its area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method that must be implemented by all subclasses.
        Each shape should return its area.
        """
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * abs(self.__radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.__radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2


def shape_info(self):
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")
