#!/usr/bin/python3
"""
This module defining the Square class.
"""


class Square:
    """
    A class used to represent a Square.
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
