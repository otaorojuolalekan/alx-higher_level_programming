#!/usr/bin/python3

def no_c(my_string):
    new_list = [i for i in my_string if i.lower() != 'c']
    new_str = ''.join(new_list)
    return new_str
