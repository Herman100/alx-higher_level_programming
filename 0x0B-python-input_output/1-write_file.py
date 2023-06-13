#!/usr/bin/python3
"""
This module defines a function that writes a string to a
text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.

    Raises:
        None

    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
