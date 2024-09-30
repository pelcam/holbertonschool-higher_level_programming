#!/usr/bin/python3
"""
This module contain the method for the task 2
"""


def append_write(filename="", text=""):
    """
    Method to appends a string at the end of a text file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
