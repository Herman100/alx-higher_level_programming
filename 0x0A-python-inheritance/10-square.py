#!/usr/bin/python3
"""
This module defines a class named Square that inherits via Rectangle
and includes an __init__ method that takes one argument: size.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class named Square that inherits via Rectangle and includes
    an __init__ method that takes one argument: size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
