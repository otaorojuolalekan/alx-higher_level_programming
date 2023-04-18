#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 3 - Write a function that returns the JSON
representation of an object (string):
"""
import json


def from_json_string(my_str):
    """
    This function returns the JSON
     representation of an object (string):
    """
    return json.loads(my_str)
