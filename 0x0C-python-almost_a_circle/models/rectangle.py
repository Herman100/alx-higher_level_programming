#!/usr/bin/python3
"""This module defines the Rectangle class that inherits fr0m Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits fr0m Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of the rectangle. Defaults to 0.
            y (int, optional): y coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle instance.

        Args:
            *args: Variable length argument list. If non-empty, assigns
                the first element to id, the second to width, the third to
                height, the fourth to x, and the fifth to y.
            **kwargs: Arbitrary keyword arguments. If args is empty,
                assigns the value of 'id' to id, 'width' to width,
                'height' to height, 'x' to x, and 'y' to y.
        """
        if len(args) >= 1:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if len(args) >= 2:
            self.width = args[1]
        elif 'width' in kwargs:
            self.width = kwargs['width']
        if len(args) >= 3:
            self.height = args[2]
        elif 'height' in kwargs:
            self.height = kwargs['height']
        if len(args) >= 4:
            self.x = args[3]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if len(args) >= 5:
            self.y = args[4]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def display(self):
        """Prints a visual representation of the Rectangle instance using
        the '#' character.
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
