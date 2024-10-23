#!/usr/bin/python3
"""
This module provides a function that returns True
if the object is an instance of, or if the object
is an instance of a class that inherited from the specified class
otherwise, False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is the same type as a_class.

    Parameters:
    obj: the object to compare
    a_class: the class to compare

    Returns:
    None
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
