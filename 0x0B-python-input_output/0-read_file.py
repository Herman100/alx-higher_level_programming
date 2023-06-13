#!/usr/bin/python3
"""
Module: file_reader

This module provides a function to read a text file
and print its contents to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
