#!/usr/bin/python3
"""
This module contain aa method to print a file to stdout.
"""


def read_file(filename=""):
    """
    Method used to read and print a file to stdout.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
