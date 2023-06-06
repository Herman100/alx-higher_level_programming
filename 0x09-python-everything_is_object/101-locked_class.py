#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    A class that only allows the creation of an
    instance attribute called 'first_name'
    """
    __slots__ = ['first_name']
