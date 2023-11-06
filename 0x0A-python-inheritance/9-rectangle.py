#!/usr/bin/python3
"""Defines a Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the rectangle instance"""
        return self.__width * self.__height