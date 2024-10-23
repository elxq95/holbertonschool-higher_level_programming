#!/usr/bin/python3
"""This module handles a function that returns
an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    '''
    This function returns an object (Python data structure)
    represented by a JSON string

    Return: object(string)
    '''
    my_json = json.loads(my_str)
    return (my_json)
