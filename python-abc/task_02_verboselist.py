#!/usr/bin/python3
"""
Module containing the VerboseList class, which extends the built-in list with verbose output.
"""


class VerboseList(list):
    """
    VerboseList class that inherits from the built-in list and provides verbose output for list operations.
    """

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
