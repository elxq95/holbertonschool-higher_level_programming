#!/usr/bin/python3
"""This module handles a function that appends a string
at the end of a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    '''
    This function appends a string at the end of a
    text file
    
    Return: the number of characters added
    '''
    with open(filename,'a', encoding="utf-8") as op:
        op.write(text)
        return (len(text))
