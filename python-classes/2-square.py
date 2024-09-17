#!/usr/bin/python3
"""
Module 2-square
Defines a class square with a private instance attribute"""

class Square:
    """
    A class that defines a square by its size
    Attributes:
    the size of the square (private attribute)"""
    def __init__(self, size):
        """
        initializes a new square instance
        Args:
            the size of the square.
            """
        self.__size = size
        if size < 0:
            raise ValueError
        if size != int(size):
            raise TypeError

        
