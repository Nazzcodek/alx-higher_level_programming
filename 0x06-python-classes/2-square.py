#!/usr/bin/python3

"""
This is a class Square
"""


class Square:
    """
    Initilizing the square object

    size: size of the square
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
