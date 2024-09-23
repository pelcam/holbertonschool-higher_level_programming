#!/usr/bin/python3

"""
module containing the Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    this class represent a rectangle, and is initiated with width an height
    """

    def __init__(self, width, height):

        """
        init width and height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
