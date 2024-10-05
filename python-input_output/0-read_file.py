#!/usr/bin/python3

#!/usr/bin/python3
"""This module handles a function that read text in a given file
"""


def read_file(filename=""):
    '''
    This function prints contents from the given file using "with"
    and open()
    The last line must skip the new line
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
