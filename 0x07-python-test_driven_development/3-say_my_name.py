#!/usr/bin/python3
"""
This module contains a function that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name given a first name and an optional last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    first_name = first_name.strip()
    last_name = last_name.strip()
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name}")
    elif last_name:
        print(f"My name is {last_name}")
    else:
        print("My name is")
