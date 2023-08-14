#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Base geometry"""

    def area(self):
        """Exception Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates as integer

        Args:
            name (str): The param name
            value (int): The param to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
