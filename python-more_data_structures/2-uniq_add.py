#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = []
    for num in my_list:
        #for each number in my_list, we check if it is
        #already in unique_integers. If not, we append it to
        #unique integers
        if num not in unique_integers:
            unique_integers.append(num)
    return sum(unique_integers)
