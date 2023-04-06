#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    num = -number
    rmdr = -(num % 10)
else:
    num = number
    rmdr = num % 10

if rmdr > 5:
    footxt = "and is greater than 5"
elif rmdr == 0:
    footxt = "and is 0"
elif rmdr < 6 and rmdr != 0:
    footxt = "and is less than 6 and not 0"

print(f"Last digit of {number} is {rmdr} {footxt}")
