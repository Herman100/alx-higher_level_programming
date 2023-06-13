#!/usr/bin/python3
"""
This module provides a function to return the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure for JSON serialization of an object.

    :param obj: An instance of a class.
    :return: The dictionary description of the object.
    """
    return obj.__dict__
