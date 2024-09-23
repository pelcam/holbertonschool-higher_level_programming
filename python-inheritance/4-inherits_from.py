#!/usr/bin/python3
"""
This module contain a function that check if the object is an instance of a
class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Function that check if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
