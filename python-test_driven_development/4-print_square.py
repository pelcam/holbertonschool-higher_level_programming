#!/usr/bin/python3
"""
Contain the function
"""
def print_square(size):
    """
    print size square
    size: value at print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
