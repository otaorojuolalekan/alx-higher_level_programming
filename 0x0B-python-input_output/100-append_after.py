#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string
    """
    # set replacer text to exchange with \n if string is found
    replacer = "\n" + new_string

    # empty txtlist to store array of modified lines
    txtlist = []

    # open file
    with open(filename, "r", encoding="UTF-8") as fp:
        for line in fp:
            if search_string in line:
                line = line.replace("\n", replacer)
            txtlist.append(line)
            # print(txtlist) - this was to debug
        wtr = "".join(txtlist)  # new text to write to file
    # print(wtr)    - this was to debug

    # overwrite filename with text inside wtr
    with open(filename, "w", encoding="UTF-8") as fp:
        fp.write(wtr)
