#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    nargs = len(argv) - 1
    if nargs == 0:
        print("{} arguments.".format(nargs))
    elif nargs == 1:
        print("{} argument:".format(nargs))
        print("{}: {}".format(nargs, argv[1]))
    else:
        print("{} arguments:".format(nargs))
        for i in range(1, nargs + 1):
            print("{}: {}".format(i, argv[i]))
