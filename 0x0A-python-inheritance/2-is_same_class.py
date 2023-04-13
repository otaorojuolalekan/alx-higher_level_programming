#!/usr/bin/python3
"""
module containing scripts
for task 2
"""


def is_same_class(obj, a_class):
    """
    this function returns true if obj
    is exactly an instance of a_class
    else it returns false
    """
    if a_class != object and  isinstance(obj, a_class):
        return True
    return False
