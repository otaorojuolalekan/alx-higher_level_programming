#!/usr/bin/python3
"""this module has a class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a square using Rectangle
    """

    def __init__(self, size):
        """
         Initialization of Rectangle params.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
