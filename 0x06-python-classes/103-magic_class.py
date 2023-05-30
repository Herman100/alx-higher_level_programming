#!/usr/bin/python3

"""
This module defines the MagicClass which represents a circle with radius.
"""

import math


class MagicClass:
    """
    The MagicClass represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
