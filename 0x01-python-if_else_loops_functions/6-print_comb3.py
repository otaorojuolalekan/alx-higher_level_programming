#!/usr/bin/python3

for a in range(48, 58):
    for b in range(48, 58):
        if chr(a) == chr(b) or chr(b) <= chr(a):
            continue
        else:
            print("{}{}".format(chr(a), chr(b)), end='')

            if (a == 56 and b == 57):
                continue
            else:
                print("{} ".format(chr(44)), end='')
print("")
