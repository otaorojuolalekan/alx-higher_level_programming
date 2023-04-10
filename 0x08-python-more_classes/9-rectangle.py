#!/usr/bin/python3
"""
Everything in previous tasks in addition to:
    Class method def square(cls, size=0):
        that returns a new Rectangle instance with
        width == height == size
"""


class Rectangle:
    """
    This class does what has already been said in
    the module doc_string above.
    Arguments:
      number_of_instances (int): the number of Rectangle instances
      print_symbol (any): changes print symbol as appropriate
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.number_of_instances += 1

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
        pr_sym2str = str(self.print_symbol)  # input of print symbol to string
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_return = []
        for i in range(self.__height):
            [rect_return.append(pr_sym2str) for j in range(self.__width)]
            if i != self.__height - 1:
                rect_return.append("\n")
        return ("".join(rect_return))

    def __repr__(self):
        """Returns formal reproducable string of the class"""
        sw = str(self.__width)
        sh = str(self.__height)
        ret_str = "Rectangle(" + sw + ", " + sh + ")"
        return ret_str

    def __del__(self):
        """class deletion method"""
        print("Bye rectangle...")
        self.number_of_instances -= 1

    def __ge__(self, other):
        ">= magic method for comparing 2 instances"
        return self.area() >= other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method for comparing 2 instances (uses __ge__)"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.__ge__(rect_1, rect_2):
            return rect_1
        else:
            return rect_2

    def __new__(cls, width, height):
        """magic method that creates a new Rectangle instance"""
        return super().__new__(width, height)

    @classmethod
    def square(cls, size=0):
        """class method that returns the new Rectangle instance created"""
        return Rectangle.__new__(size, size)


"""     @classmethod
    def square(cls, size=0):
        "Class method that returns a new rectangle"
        return cls(size, size) """
