#!/usr/bin/python3
"""
The AirBnB project is a big part of the Higher level curriculum.
This project will help you be ready for it.
All previous lessons learnt will come to use here.
"""


class Base:
    """
    This is the base class of the Airbnb mini project
    Attrs:
        nb_objects --> private attribute
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        instantiation for Base class
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
