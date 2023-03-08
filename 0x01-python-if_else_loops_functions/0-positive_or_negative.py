#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    txtfield = "is positive"
elif number == 0:
    txtfield = "is zero"
else:
    txtfield = "is negative"
print(f"{number} {txtfield}")
