#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """MyInt that inherits from int"""

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value):
        """Override == with != operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != with == operator"""
        return self.real == value
