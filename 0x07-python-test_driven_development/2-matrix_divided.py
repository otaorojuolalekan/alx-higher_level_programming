#!/usr/bin/python3
"""
   This module contains a function that...
   divides all elements of a matrix by a number (div)
   All possible test cases will be listed here.
    - matrix not a list
    - matrix not a list of lists.
    - elements of matrix not integers or floats
    - each row of matrix not same size
    - div not integer or float
    - div == ZERO
"""


def matrix_divided(matrix, div):
    """ Function to divide matrix by div
    Returns a matrix containing elements that have...
    ...each been divided by div.
    Raises appropriate errors for appropriate exceptions.
        TypeError - if not list of list or div non integer/float
        ZeroDivisionError - if div == Zero
    """

    # matrix not a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # div not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # div not int or float

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    # matrix not a list of lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        else:       # calculate length of first matrix row
            rowlen = len(matrix[0])
            if len(row) != rowlen:
                raise TypeError("Each row of the matrix must have "
                                "the same size")
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix (list "
                                "of lists) of integers/floats")
    return [[round((i / div), 2) for i in row] for row in matrix]
