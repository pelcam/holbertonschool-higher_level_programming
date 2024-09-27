#!/usr/bin/python3
"""
Module containing the Dragon class. Vive les dragons!
"""


class SwimMixin:
    """
    Mixin class that provides swimming ability.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class. Agrougrou!
    Inherits swimming and flying abilities from SwimMixin and FlyMixin.
    """

    def roar(self):
        print("The dragon roars!")
