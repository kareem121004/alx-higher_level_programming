#!/usr/bin/python3
""" lass Student"""


class Student:
    """ lass Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:

            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__setattr__(key, value)
