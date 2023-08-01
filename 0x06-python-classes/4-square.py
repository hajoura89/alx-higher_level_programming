#!/usr/bin/python3

"""An empty class Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Instantiation with size

        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set value to the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)
