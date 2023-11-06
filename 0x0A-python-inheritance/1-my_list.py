#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        print(sorted(self))
