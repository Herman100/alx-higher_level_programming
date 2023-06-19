#!/usr/bin/python3
"""Module for Base class"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class

        Args:
            id (int, optional): id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            str: the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances that inherit from Base
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))
