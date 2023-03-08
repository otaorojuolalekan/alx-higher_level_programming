#!/usr/bin/python3

def uppercase(str):
    str_upp = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        str_upp += ch
    print("{}".format(str_upp))
