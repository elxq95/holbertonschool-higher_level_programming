#!/usr/bin/python3
"""
This module provides a function that returns True
if the object is exactly an instance of the specified class
otherwise, False
"""


def is_same_class(obj, a_class):
    """
    Check if the object is the same type as a_class.

    Parameters:
    obj: the object to compare
    a_class: the class to compare

    Returns:
    None
    """
    if (type(obj) is a_class):
        return True
    else:
        return False
