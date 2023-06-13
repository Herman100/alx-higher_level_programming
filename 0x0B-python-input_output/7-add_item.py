#!/usr/bin/python3
"""
This module provides a script to add all arguments to
a Python list and save them to a file.
"""


import sys
from os import path


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    :param my_obj: The object to serialize.
    :param filename: The name of the file to write to.
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    :param filename: The name of the file to read from.
    :return: The deserialized object.
    """
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


filename = "add_item.json"
my_list = []

if path.exists(filename):
    my_list = load_from_json_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
