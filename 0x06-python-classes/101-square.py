#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object with a given size and position.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square using '#'.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        square_str = ""
        if self.__size == 0:
            return square_str
        for _ in range(self.__position[1]):
            square_str += "\n"
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str[:-1]  # Remove the last newline


if __name__ == "__main__":
    """
    Create and test Square objects.
    """
    my_square = Square(5, (2, 1))
    print(my_square)  # Output: \n\n  #####\n  #####\n  #####\n  #####\n  #####
    print(my_square.area())  # Output: 25

    my_square.size = 3
    my_square.position = (1, 2)
    my_square.my_print()
    """
      ###
      ###
      ###
    """
