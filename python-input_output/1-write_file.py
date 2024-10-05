#!/usr/bin/python3
"""This module handles a function that write a given text in a given file
"""

def write_file(filename="", text=""):
    '''
    This function writes contents from the given file using "with"
    and open() and write()
    '''
    with open(filename,'w', encoding="utf-8") as op:
        op.write(text)
    return (len(text))
