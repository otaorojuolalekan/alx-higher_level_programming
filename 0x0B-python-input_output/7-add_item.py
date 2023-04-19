#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 7 - Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file
    filename = "add_item.json"

    # load list_items from filename. if not exist return empty list
    try:
        list_items = load_from_json_file(filename)
    except FileNotFoundError:
        list_items = []

    # add command line arguments to list items
    list_items.extend(sys.argv[1:])

    # add list items add_item.json file
    save_to_json_file(list_items, filename)
