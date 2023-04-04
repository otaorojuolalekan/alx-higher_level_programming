#!/usr/bin/python3
"""Module to Say my Name
returns predefined text + name"""


def say_my_name(first_name, last_name=""):
    """
    Arguments:
    first_name: 1st argument
    last_name: 2nd argument
    Raises:
    TypeError: if either argument is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    elif not(last_name):
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
