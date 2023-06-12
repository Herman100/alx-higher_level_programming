#!/usr/bin/python3

"""
This module defines a class MyList that inherits from
list and has a method to print the list in ascending order.
"""


class MyList(list):
    """
    A class that inherits from list and has a method
    to print the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
