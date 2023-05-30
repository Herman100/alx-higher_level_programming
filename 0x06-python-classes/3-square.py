#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Square class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a new Square object

        Args:
            size (int): The size of the new square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area"""
        return self.__size ** 2
