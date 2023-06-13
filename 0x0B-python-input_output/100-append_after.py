#!/usr/bin/python3
"""
This module provides a function to insert a line of text into
a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file
    after each line containing a specific string.

    :param filename: The name of the file to modify.
    :param search_string: The string to search for in the file.
    :param new_string: The string to insert into the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
