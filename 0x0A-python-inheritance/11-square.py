#!/usr/bin/python3
"""Defines a Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
    
    def area(self):
        """Computes the area of a Square instance"""
        return self.__size ** 2
