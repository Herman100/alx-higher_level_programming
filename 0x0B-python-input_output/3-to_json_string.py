#!/usr/bin/python3
"""
This module provides a function to serialize
an object into a JSON-formatted string.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The object to serialize.
    :return: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
