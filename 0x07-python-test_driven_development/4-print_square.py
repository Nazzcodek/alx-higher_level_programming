#!/usr/bin/python3

"""
This is the module for the print_square function
"""


def print_square(size):
    """
    The print_square function

    Params:
        size: the lenght and breath of the sqaure

    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    print:
        a string of # symbols with length of size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
