#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list[:]

    for num in new_list[0:]:
        if num % 2 == 0:
            return True

    return new_list
