#!/usr/bin/python3

"""An empty class Square"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)
