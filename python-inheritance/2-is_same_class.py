#!/usr/bin/python3
"""
This module contain a function to check if
a given object is an instance of a given class
"""


def is_same_class(obj, a_class):
    """
    function to check is the given object is an insatnce of the given class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
