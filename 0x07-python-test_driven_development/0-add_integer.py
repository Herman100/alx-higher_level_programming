#!/usr/bin/python3
"""
This module provides a function to add two numbers
and return the result as an integer.

Example:
    >>> from add_integer import add_integer
    >>> add_integer(1, 2)
    3
    >>> add_integer(1.0, 2.0)
    3
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    If either a or b is not an integer or float, raises a TypeError.

    Args:
        a: The first number to be added. Must be an integer or float.
        b: The second number to be added. Must be an integer or float.
        Defaults to 98.

    Returns:
        The sum of a and b, casted to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
