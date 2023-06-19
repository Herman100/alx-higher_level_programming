#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class

        Args:
            size (int): size of the square
            x (int, optional): x coordinate of the square. Defaults to 0.
            y (int, optional): y coordinate of the square. Defaults to 0.
            id (int, optional): id of the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square object"""
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square object

        Args:
            *args: variable-length argument list
            **kwargs: arbitrary keyword arguments
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
