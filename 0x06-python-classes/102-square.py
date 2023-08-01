#!/usr/bin/python3

"""An empty class Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Instantiation

        Args:
            size (int): The size of the new square.
        """
        self.size = size

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

    def __eq__(self, other):
        """Define the == comparision"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison"""
        return self.area() >= other.area()
