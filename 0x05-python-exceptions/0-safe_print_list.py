#!/usr/bin/python3

def lenn(my_list=[]):
    count = 0
    for i in my_list:
        count += 1
    return count


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        if x > lenn(my_list):
            raise IndexError

        for i in my_list[0:x]:
            print(i, end="")
        return x
    except IndexError:
        for i in my_list[0:lenn(my_list)]:
            print(i, end="")
        return lenn(my_list)
    finally:
        print()
