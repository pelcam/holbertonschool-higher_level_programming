#!/usr/bin/python3
"""
module with the subclass Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class that represent a square and is inherits from the subclass Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
