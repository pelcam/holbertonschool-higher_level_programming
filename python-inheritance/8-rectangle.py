#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module contain the Rectangle subclass from the class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    this class represent a rectangle, and is initiated with width an height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
