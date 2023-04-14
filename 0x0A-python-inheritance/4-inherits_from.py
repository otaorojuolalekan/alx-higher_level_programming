#!/usr/bin/python3
"""
Module containing scripts for task 4
"""


def inherits_from(obj, a_class):
    """
    this function returns true if obj is a subclass
    of a_class, otherwise false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
