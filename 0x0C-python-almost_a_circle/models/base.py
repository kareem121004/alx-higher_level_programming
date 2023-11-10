#!/usr/bin/python3
"""This module implements `base` class"""


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
