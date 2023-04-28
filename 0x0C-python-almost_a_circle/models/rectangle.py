#!/usr/bin/python3
"""
Contains class rectangle that inherits from base
"""
from models.base import Base
import sys


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and Setter for width attribute
    @property
    def width(self):
        """
        Getter Method for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Method for width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and Setter for height attribute
    @property
    def height(self):
        """
        Getter Method for width attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter Method for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and Setter for x attribute
    @property
    def x(self):
        """
        Getter Method for width attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter Method for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and Setter for y attribute
    @property
    def y(self):
        """
        Getter Method for width attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter Method for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        computes Area of the rectangle instance
        """
        return self.height * self.width

    def display(self):
        """
        prints the instance in stdout with char #
        Also handles vertical and horizontal offset y, x
        """
        for a in range(self.y):
            print()
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """string magic method of instance"""
        clsname = self.__class__.__name__
        args = [clsname, self.id, self.x,
                self.y, self.width, self.height]
        return "[{}] ({}) {}/{} - {}/{}".format(*args)

    def update(self, *args, **kwargs):
        """
        Update class attributes from CLI arguments
        """
        # *args - ordered list of arguments
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i >= len(attributes):
                break
            setattr(self, attributes[i], arg)

        # keyworded list of arguments
        for attribute in ['id', 'width', 'height', 'x', 'y']:
            value = kwargs.get(attribute, None)
            if value is not None:
                setattr(self, attribute, value)

    def to_dictionary(self):
        """This method returns the dictionary
        of a Rectangle instance"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }

    """ Alternate method to write (but ZEN of Python not followed)
    def update(self, *args, **kwargs):
        update the class args from CLI
        if args and len(args):
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.width = args[1]
            except IndexError:
                pass
            try:
                self.height = args[2]
            except IndexError:
                pass
            try:
                self.x = args[3]
            except IndexError:
                pass
            try:
                self.y = args[4]
            except IndexError:
                pass
        for attribute in ['id', 'width', 'height', 'x', 'y']:
            value = kwargs.get(attribute)
            if value is not None:
                setattr(self, attribute, value)
        """
