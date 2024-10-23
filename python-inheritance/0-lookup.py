#!/usr/bin/python3

"""
This module provides a utility function 
to inspect objects in Python.

The `lookup` function can be used to retrieve a list of available 
attributes and methods
of an object, providing insight into what functionality is accessible.

Example usage:
    class ExampleClass:
        def example_method(self):
            pass

    example_instance = ExampleClass()
    print(lookup(example_instance))
"""

def lookup(obj):
    """
    Returns the list of available attributes and 
    methods of an object.

    This function provides introspection capabilities 
    by returning all the attributes
    and methods associated 
    with the given object `obj`. It does not rely on any external
    modules and utilizes Python's built-in `dir()` function.

    Parameters:
    obj (any): The object whose attributes and 
    methods are to be retrieved.

    Returns:
    list: A list containing the names of attributes
    and methods available for `obj`.
    """
    return dir(obj)
