#!/usr/bin/python3
"""
Task 2 scripts
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as ftw:
        return ftw.write(text)
