#!/usr/bin/python3
"""
This module defines a function named add_attribute that adds a new
attribute to an object if it's possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    :param obj: The object to add the attribute to.
    :type obj: any
    :param name: The name of the attribute to add.
    :type name: str
    :param value: The value of the attribute to add.
    :type value: any
    :raises TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
