#!/usr/bin/python3

"""
This is the module for Rectangle class
"""


class Rectangle(BaseGeometry):
    """This is a child class to BaseGeometry"""

    def __init__(self, width, height):
        """ Initialize the instance
            Params:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width