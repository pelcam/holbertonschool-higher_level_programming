#!/usr/bin/python3
"""
This module contain a function to check if
a given object is an instance of a given class
"""


def is_same_class(obj, a_class):
    """
    function to check is the given object is
    exactly an instance of the given class
    """
    return type(obj) == a_class
