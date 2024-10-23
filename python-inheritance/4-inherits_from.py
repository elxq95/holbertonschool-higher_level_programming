#!/usr/bin/python3
"""
This module provides a function that returns True
if the object is an instance of a class that inherited
 (directly or indirectly) from the specified class
otherwise, False
"""


def inherits_from(obj, a_class):
    """
    Check if the object if the object is an instance
    of a class that inherited
    (directly or indirectly) from the specified class

    Parameters:
    obj: the object to compare
    a_class: the class to compare

    Returns:
    None
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
