#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 3 - Write a function that returns the JSON
representation of an object (string):
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation:
    """
    with open(filename, "w", encoding="UTF-8") as fp:
        json.dump(my_obj, fp)
