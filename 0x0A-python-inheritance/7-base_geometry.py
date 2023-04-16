#!/usr/bin/python3
"""
This module contains an empty geometry class
"""


class BaseGeometry:
    """
    the empty geometry class
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
