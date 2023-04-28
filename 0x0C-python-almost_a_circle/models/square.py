#!/usr/bin/python3
"""
Contains class square that inherits from Rectangle
"""
from models.rectangle import Rectangle
import sys


class Square(Rectangle):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of child class params"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method for Square class"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if arg is not None:
                    # print("attr[i] = {} & arg = {}".format(attributes[i], arg))
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                if v is not None:
                    setattr(self, k, v)

    def to_dictionary(self):
        """dictionary method for Square"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size
        }

    def __str__(self):
        args = [self.__class__.__name__, self.id,
                self.x, self.y, self.width]
        return "[{}] ({}) {}/{} - {}".format(*args)
