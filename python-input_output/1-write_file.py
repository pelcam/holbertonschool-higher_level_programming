#!/usr/bin/python3
"""
Module with a method for the task 1.
"""


def write_file(filename="", text=""):
    """
    Method used to create a file and write in it.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
