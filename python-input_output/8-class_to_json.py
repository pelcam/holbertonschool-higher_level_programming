#!/usr/bin/python3
"""
Module with function for task 8.
"""
import json


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure for JSON serialization of an object.
    """

    obj_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (str, int, float, bool, list, dict)):
            obj_dict[attr] = value
    return obj_dict
