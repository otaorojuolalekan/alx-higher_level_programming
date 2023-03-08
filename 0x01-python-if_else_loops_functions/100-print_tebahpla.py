#!/usr/bin/python3

count = 0
for i in range(122, 96, -1):
    count += 1
    ch = chr(i)
    if count % 2 == 0:
        print("{}".format(ch.upper()), end='')
    else:
        print("{}".format(ch), end='')
