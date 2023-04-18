#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 2 - appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding='UTF-8') as myfile:
        fc = myfile.write(text)
        return fc
