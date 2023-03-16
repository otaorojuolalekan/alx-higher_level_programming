#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    keylist = [k for k, v in a_dictionary.items() if v == value]
    for key in keylist:
        del(a_dictionary[key])
    return a_dictionary
