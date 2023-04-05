#!/usr/bin/python3
"""
  Print Square Module
  - (using # as building blocks for the square)
"""


def print_square(size):
    """
    Function to print square
    using # as building blocks
    Argument:
    size - only argument to expect, no defaults
    Raises:
    TypeError: if size not int or < 0
    """

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(size * '#')
