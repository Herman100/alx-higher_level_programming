#!/usr/bin/python3
"""
This module provides a function to deserialize
a JSON-formatted string into a Python object.
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to deserialize.
    :return: The deserialized object.
    """
    return json.loads(my_str)
