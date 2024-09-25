#!/usr/bin/python3

def lookup(obj):
    """
    This function returns the list of available attributes and methods of an object.
    
    Parameters:
    obj: The object to inspect.
    
    Returns:
    list: A list containing the names of attributes and methods.
    """
    return dir(obj)
