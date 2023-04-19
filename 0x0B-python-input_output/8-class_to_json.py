#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 8 - Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    This function returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean)
    for JSON serialization of an object
    """
    return (obj.__dict__)

# if __name__ == "__main__":
#     save_to_json_file = \
#         __import__("5-save_to_json_file").save_to_json_file
#     load_from_json_file = \
#         __import__("6-load_from_json_file").load_from_json_file
