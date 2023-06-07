#!/usr/bin/python3
"""
This module provides a function to indent text by adding two newlines after
each occurrence of the characters '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Indent text by adding two newlines after
    each occurrence of '.', '?' and ':'.

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))
