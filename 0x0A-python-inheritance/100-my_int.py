#!/usr/bin/python3
"""
This module defines a class named MyInt that inherits fr0m int
and has its == and != operators inverted.
"""


class MyInt(int):
    """
    A class named MyInt that inherits fr0m int and has its
    == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Returns True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Returns True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
