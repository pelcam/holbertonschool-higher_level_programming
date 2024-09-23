#!/usr/bin/python3
"""
This module contain a function that check if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
