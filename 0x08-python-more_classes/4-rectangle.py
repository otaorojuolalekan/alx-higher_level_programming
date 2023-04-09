#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 3-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError
exception with the message width must be an integer
if width is less than 0, raise a ValueError exception
with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception
with the message height must be an integer
if height is less than 0, raise a ValueError exception
with the message height must be >= 0
Instantiation with optional width and height:
def __init__(self, width=0, height=0):
Public instance method: def area(self):
that returns the rectangle area
Public instance method: def perimeter(self):
that returns the rectangle perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #:
(see example below)
if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle
to be able to recreate a new instance by using eval()
(see example below)
You are not allowed to import any module
"""


class Rectangle:
    """
    This class does what has already been said in
    the module doc_string above.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter
        REQ: must return 0 if either input is 0
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of the class"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_return = []
        for i in range(self.__height):
            [rect_return.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_return.append("\n")
        return ("".join(rect_return))

    def __repr__(self):
        """Returns formal reproducable string of the class"""
        sw = str(self.__width)
        sh = str(self.__height)
        ret_str = "Rectangle(" + sw + ", " + sh + ")"
        return ret_str
