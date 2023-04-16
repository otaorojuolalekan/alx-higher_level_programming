#!/usr/bin/python3
"""
module containing the scripts
for task 1
"""


class MyList(list):
    """A class that inherits from
    the python builtin class of list
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        function of child Mylist to print sorted
        """
        print(sorted(self))
