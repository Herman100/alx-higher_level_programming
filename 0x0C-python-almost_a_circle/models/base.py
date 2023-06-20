#!/usr/bin/python3
"""Module for Base class"""
import json
import os
import csv


class Base:
    """Base class for other classes in the project"""

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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        The filename must be: <Class name>.json - example: Rectangle.json

        Returns:
            list: If the file doesn't exist, returns an empty list.
                Otherwise, returns a list of instances of the class.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            json_str = f.read()

        list_of_dicts = cls.from_json_string(json_str)
        return [cls.create(**d) for d in list_of_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer.writerow(fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                instance_dict = {}
                for field, value in zip(header, row):
                    instance_dict[field] = int(value)
                instances.append(cls.create(**instance_dict))
        return instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs:
            list_dicts = [o.to_dictionary() for o in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: If json_string is None or empty, returns an empty list.
                Otherwise, returns the list represented by json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary: A double pointer to a dictionary containing
                key-value pairs of attributes to be set.

        Returns:
            Base: An instance of the class with all attributes set according
                to the key-value pairs in dictionary.
        """
        # Create a dummy instance with default values for mandatory attributes
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        # Update the dummy instance with the values in dictionary
        dummy.update(**dictionary)

        return dummy
