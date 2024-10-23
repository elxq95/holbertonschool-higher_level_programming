#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in my_list[::-1]:
            # Use str.format() to print each integer
            print("{:d}".format(i))
