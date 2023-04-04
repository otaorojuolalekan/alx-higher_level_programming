#!/usr/bin/python3
""" Addition module:
   Adds two arguments a and b
   raise exception if not integer or float
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b
    Returns a + b
    checks if a & b are float or int, else raise TypeError
    if a or b is float, cast value to integer
    doc linescount must be 5
    """

    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if (type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
