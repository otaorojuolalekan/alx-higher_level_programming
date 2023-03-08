#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number *= -1
    lstDg = number % 10
    print("{:d}".format(lstDg), end='')
    return (lstDg)
