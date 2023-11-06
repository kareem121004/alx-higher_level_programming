#!/usr/bin/python3
"""Defines a MyInt"""


class MyInt(int):
    """Represents a MyInt"""

    def __eq__(self, other):
        """Equality becomes inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality"""
        return super().__eq__(other)
