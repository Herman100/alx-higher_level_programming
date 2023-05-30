#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class that defines a square by its size"""

    def __init__(self, size):
        """Initialize a new Square object

        Args:
            size (int): The size of the new square
        """
        self.__size = size
