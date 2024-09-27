#!/usr/bin/python3
"""
This module provides a CountedIterator class that counts
elements in iterable item and update the current count
"""
class CountedIterator:
    """
    class CountedIterator inherited from list class
    """
    def __init__(self, iterator, counter=0):
        self.__iterator = iter(iterator)
        self.__counter = counter

    def get_count(self):
        return self.__counter

    def __next__(self):
        next_item = next(self.__iterator)
        self.__counter += 1
        return next_item
