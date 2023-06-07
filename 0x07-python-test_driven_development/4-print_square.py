#!/usr/bin/python3
"""
This module contains a function that prints
a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.
    :param size: size length of the square
    :type size: int
    :raises TypeError: if size is not an integer
    :raises ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
