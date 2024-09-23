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

    if isinstance(obj, a_class):
        return True
    else:
        return False
