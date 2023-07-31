#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Function that prints an integer.

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        True if value has been correctly printed
        Otherwise, False and prints in stderr the error precede by Exception
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
