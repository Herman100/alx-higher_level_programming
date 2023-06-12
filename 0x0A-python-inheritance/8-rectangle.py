#!/usr/bin/python3
"""
This module defines a class named Rectangle that inherits
BaseGeometry and includes an __init__ method
that takes two arguments: width and height.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class named Rectangle that inherits
    BaseGeometry and includes
    an __init__ method that takes two arguments: width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the given width and height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
