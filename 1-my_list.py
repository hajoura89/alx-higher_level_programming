#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Mylist that inherits from list"""
    def __init__(self):
        """Initialization of the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
