#!/usr/bin/python3
"""
This module contain the CustomObject class
"""
from pickle import load, dump


class CustomObject:
    """
    Class that is a custom object
    """

    def __init__(self, name, age, is_student):
        """
        init function
        """

        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def display(self):
        """
        Display the attributes of an object
        """

        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        """
        Serialize an object
        """

        try:
            with open(filename, "wb") as f:
                dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a given file
        """

        try:
            with open(filename, "rb") as f:
                return load(f)
        except Exception as e:
            return None
