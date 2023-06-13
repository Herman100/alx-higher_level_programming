#!/usr/bin/python3
"""
This module provides a function to create an object from a "JSON file".
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    :param filename: The name of the file to read from.
    :return: The deserialized object.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
