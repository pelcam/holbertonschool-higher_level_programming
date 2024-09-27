#!/usr/bin/python3
"""
Module containing the CountedIterator class which tracks the number of iterations.
"""


class CountedIterator:
    """
    Iterator that tracks the number of items it has iterated over.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count

    def __iter__(self):
        return self
