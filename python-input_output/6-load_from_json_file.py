#!/usr/bin/python3
"""
Module with funciton for task 6.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        x = f.read()
    return json.loads(x)
