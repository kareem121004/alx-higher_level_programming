#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Defines a function that reads a file"""

    with open(filename, 'r', encoding='utf-8') as f:
        print("{}".format(f.read()), end="")
