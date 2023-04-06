#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
nargs = len(av) - 1
summ = 0
if nargs >= 1:
    for i in range(1, nargs + 1):
        summ += int(av[i])
print(summ)
