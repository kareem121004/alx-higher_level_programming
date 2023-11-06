#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """func to check"""

    return isinstance(obj, a_class) and type(obj) != a_class
