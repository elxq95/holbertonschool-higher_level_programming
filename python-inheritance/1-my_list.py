#!/bin/usr/python3
class MyList(list):
    """
    A subclass of the built-in list that includes an additional method to print the list in sorted order.
    """


    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        Assumes all elements of the list are of type int.
        """
        sorted_list = sorted(self)
        print(sorted_list)
