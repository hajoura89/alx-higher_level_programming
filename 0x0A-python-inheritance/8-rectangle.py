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
