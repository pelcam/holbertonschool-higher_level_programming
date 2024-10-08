#!/usr/bin/python3
"""
Module containing the Animal abstract class and concrete Dog and Cat classes.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class for all animals.
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class that implements the sound method.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class that implements the sound method.
    """

    def sound(self):
        return "Meow"
