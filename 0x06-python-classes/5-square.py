#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Method for initializing a square object with a given size"""
        self.size = size

    @property
    def size(self):
        """Getter method for the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size property"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Method that prints the square using the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
