#!/usr/bin/python3
"""
Module containing the Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, an 'abomination of nature.'
    Inherits behavior from both Fish and Bird classes.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
