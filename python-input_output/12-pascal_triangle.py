#!/usr/bin/python3
"""
Module with function for task 12.
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """

    global_list = []
    if n <= 0:
        return global_list

    for x in range(n + 1):
        list_added = []
        for y in range(x + 1):
            list_added.append(y)
        global_list.append(list_added)

    return global_list
