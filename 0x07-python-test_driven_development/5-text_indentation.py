#!/usr/bin/python3
"""
This module has a function that prints a text with
2 new lines after each of these characters: ., ? and :
REQUIREMENTS
-  Prototype: def text_indentation(text):
-  text must be a string, otherwise raise a TypeError exception
  with the message text must be a string
-  There should be no space at the beginning or at the end of each printed line
-  You are not allowed to import any module
"""


def text_indentation(text):
    """
    This function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Argument:
      text: has to be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    # iterate through text and replace each occurrence with \n\n

    checklist = ['.', '?', ':']
    for ch in checklist:
        text = text.replace(ch, ch + "\n\n")

    # split by new lines

    lines = text.split("\n")
    # strip all leading and trailing spaces
    for line in lines:
        print(line.strip())
