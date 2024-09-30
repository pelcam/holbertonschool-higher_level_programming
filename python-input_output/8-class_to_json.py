#!/usr/bin/python3
"""
Module with function for task 8.
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure for JSON serialization of an object.
    """

    return obj.__dict__
