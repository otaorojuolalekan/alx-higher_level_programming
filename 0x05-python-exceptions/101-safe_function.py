#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except (TypeError, NameError, ValueError, ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
