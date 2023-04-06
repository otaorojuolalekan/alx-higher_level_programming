#!/usr/bin/python3

def max_integer(my_list=[]):
    listlen = len(my_list)
    if listlen == 0:
        return (None)
    else:
        max1 = my_list[0]
        for i in range(listlen):
            if my_list[i] > max1:
                max1 = my_list[i]
    return (max1)
