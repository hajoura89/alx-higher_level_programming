#!/usr/bin/python3
"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inheriting BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of a new Rectangle

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print() and str() of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
