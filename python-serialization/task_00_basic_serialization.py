#!/usr/bin/python3
"""
Module with function to serialize an deserialize data
"""
from pickle import load, dump


def serialize_and_save_to_file(data, filename):
    """
    This function serialize json data
    """

    with open(filename, "wb") as f:
        dump(data, f)


def load_and_deserialize(filename):
    """
    This function deserialize json data
    """

    with open(filename, "rb") as f:
        return load(f)
