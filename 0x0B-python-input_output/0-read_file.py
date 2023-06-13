#!/usr/bin/python3
"""
Module: file_reader

This module provides a function to read a text file
and print its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: The name of the file to read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
