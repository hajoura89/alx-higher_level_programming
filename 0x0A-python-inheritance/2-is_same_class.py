#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
