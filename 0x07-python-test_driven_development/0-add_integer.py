#!/usr/bin/python3

"""
This is the module for the add_integer function
"""

def add_integer(a, b=98):
    """ 
    Function to add param
    Params:
        a: the first param (must be integer or float)
        b: the second param (must be integer or float)
    Raise:
        TypeError: when either a or b is not int or float
    Return:
        The integer of the addition of a and b 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
