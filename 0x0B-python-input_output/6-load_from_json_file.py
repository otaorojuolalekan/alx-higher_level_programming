#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 6 - Write a function that creates
an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”:
    """
    with open(filename, "r", encoding="UTF-8") as filestream:
        jsconv = json.load(filestream)
    return jsconv
