#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers a and b
    Returns a + b
    checks if a & b are float or int, else raise TypeError
    if a or b is float, cast value to integer
    doc linescount must be 5
    """
    if type(a) in [int, float]:
        if(type(a) == float):
            a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        if(type(b) == float):
            b = int(b)
    else:
        raise TypeError("b must be an integer")
    
    return (a + b)