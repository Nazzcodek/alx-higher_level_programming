#!/usr/bin/python3

"""
This is the module for Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a Square object that inherit from 9-rectangle
    """
    def __init__(self, size):
        """
        Initialization of the instance

        Params:
            size: size of the square
        """
        self.__size = size
        self.integer_validator('size', size)

    """ public instance"""
    def area(self):
        return self.__size ** 2

    """ sting instance """
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
