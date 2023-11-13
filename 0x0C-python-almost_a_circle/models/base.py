#!/usr/bin/python3
"""This module implements `base` class"""

import json
import csv


class Base:
    """implementation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list to json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """transform a JSON string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new object from dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        filename = cls.__name__ + ".json"
        word = []

        if list_objs is not None:
            for lst in list_objs:
                word.append(lst.to_dictionary())    
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(word))
