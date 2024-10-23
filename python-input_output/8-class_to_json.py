#!/usr/bin/python3
"""This module returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Return: dictionary
    """
    return obj.__dict__
