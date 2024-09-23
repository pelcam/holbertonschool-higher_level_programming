#!/usr/bin/python3
"""
This module contain an empty class
"""


class BaseGeometry:
    """
    This empty class doesn't do much for now
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        return value
