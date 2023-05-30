#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a square object with a given size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the square is equal to another square based on their areas.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if the square is not equal
        to another square based on their areas.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if the square is greater than
        another square based on their areas.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the square is greater than or equal
        to another square based on their areas.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the square is less than another square based on their areas.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the square is less than or equal
        to another square based on their areas.
        """
        return self.__lt__(other) or self.__eq__(other)


if __name__ == "__main__":
    """
    Create and test Square objects.
    """
    my_square_1 = Square(5)
    my_square_2 = Square(3)
    my_square_3 = Square(5)
    print(my_square_1 == my_square_2)  # Output: False
    print(my_square_1 != my_square_2)  # Output: True
    print(my_square_1 > my_square_2)  # Output: True
    print(my_square_1 >= my_square_2)  # Output: True
    print(my_square_1 < my_square_2)  # Output: False
    print(my_square_1 <= my_square_2)  # Output: False
    print(my_square_1 == my_square_3)  # Output: True
