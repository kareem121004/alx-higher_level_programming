#!/usr/bin/python3
"""This module implements a Rectangle object"""

from models.base import Base


class Rectangle(Base):
    """Rectangle implementation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance"""
        self.type_value('width', value, False)
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        self.type_value('height', value, False)
        self.__height = value

    @property
    def x(self):
        """Retrieves the x of a Rectangle instance."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x of a Rectangle instance"""
        self.type_value('x', value)
        self.__x = value

    @property
    def y(self):
        """Retrieves the y of a Rectangle instance."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y of a Rectangle instance"""
        self.type_value('y', value)
        self.__y = value

    def type_value(self, name, value, eq=True):
        """type and value validation"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.width * self.height
