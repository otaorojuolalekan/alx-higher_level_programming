#!/usr/bin/python3
"""
0x0B. Python - Input/Output
Task 7 - Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"

# get the command line arguments as a list
cmargs = sys.argv

# convert the list to json and append it to add_item.json
with open(filename, mode="a", encoding="UTF-8") as fp:
    save_to_json_file(cmargs, filename)

# load the json file content and remove sys.argv[0] i.e the scriptname
with open(filename) as fp:
    filecontent = load_from_json_file(filename)
    filecontent.remove(sys.argv[0])

# This time, overwrite filename with filecontent(which does not have scriptname)
with open(filename, mode="w", encoding="UTF-8") as fp:
    save_to_json_file(filecontent, filename)
