#!/usr/bin/python3
"""
This module contains an empty geometry class
"""


class BaseGeometry:
    """
    the empty geometry class
    """
    def __init__(self, name="", value=1):
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")
    

    def integer_validator(self, name, value):
        super().__init__()
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
