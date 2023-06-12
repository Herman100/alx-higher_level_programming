#!/usr/bin/python3
"""
This module defines a class named BaseGeometry that includes a
public instance method named area that raises an exception.
"""


class BaseGeometry:
    """
    A class named BaseGeometry that includes a public
    instance method named area that raises an exception.
    """
    def area(self):
        """
        Raises an Exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")
