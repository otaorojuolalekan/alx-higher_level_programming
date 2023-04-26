#!/usr/bin/python3
"""
Contains class rectangle that inherits from base
"""
from models.base import Base


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
        if value < 0:
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
        if value < 0:
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
        return self.__height * self.__width
