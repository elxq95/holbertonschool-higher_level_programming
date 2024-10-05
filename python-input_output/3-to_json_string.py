#!/usr/bin/python3
"""This module handles a function
that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    '''
    This function returns the JSON representation
    of an object (string)

    Return: object(string)
    '''
    my_json = json.dumps(my_obj)
    print(my_json)
