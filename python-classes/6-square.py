#!/usr/bin/python3
"""
This module defining the Square class.
"""


class Square:
    """
    A class used to represent, and print a Square at a specified location.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(a, int) and a >= 0 for a in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for y in range(self.__position[1]):
                print('')

            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
