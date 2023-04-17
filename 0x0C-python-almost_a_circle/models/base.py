#!/usr/bin/python3
"""Defines a base model class."""
import json
import os
import csv


class Base:
    """This will the blueprint of all other projects in this project
    Objective:
        Manage id attributes in all classes and
          avoid duplicating of code(& bugs)
    Attributes:
    __nb_objects (int) - this will be a counter for number
      of times base class is instantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns string representation of list dictionaries
        Args:
            list_dictionaries: is a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representationof list_objs to a file
        Args:
            cls: file the data is to be saved into
            list_obj: it is a list of objects
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as Jsonf:
            if list_objs is None:
                Jsonf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                Jsonf.write(Base.to_json_string(list_dicts))

    @classmethod
    def from_json_string(cls, json_string):
        """Returns the python format list of  JSON string"""
        Jlist = []

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantiated from a dictionary of attributes.
        Args:
        **dictionary: key/value attributes to be intialized
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        instance_list = []
        dict_list = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                my_str = f.read()
                dict_list = cls.from_json_string(my_str)
                for dictionary in dict_list:
                    instance_list.append(cls.create(**dictionary))
        return instance_list
