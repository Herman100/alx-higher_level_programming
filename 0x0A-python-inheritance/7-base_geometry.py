#!/usr/bin/python3
"""
This module defines a class named BaseGeometry that includes
two public instance methods: area and integer_validator.
"""


class BaseGeometry:
    """
    A class named BaseGeometry that includes two public
    instance methods: area and integer_validator.
    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
