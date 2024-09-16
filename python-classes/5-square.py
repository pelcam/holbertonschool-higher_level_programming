#!/usr/bin/python3
"""
This module defining the Square class.
"""


class Square:
    """
    A class used to represent a Square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

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

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for y in range(self.__size):
                for x in range(self.__size):
                    print('#', end='')
                print('\n')
