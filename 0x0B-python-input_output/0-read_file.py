#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 0 - reads a text file (UTF8) and prints it to stdout
"""

def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='UTF-8') as myfile:
        fc = myfile.read()
    print(fc)