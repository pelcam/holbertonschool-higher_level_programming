#!/usr/bin/python3
"""
Module containing the Shape abstract class and its concrete Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return abs((2 * self.radius) * pi)


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Utility function to print the area and perimeter of a given shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
