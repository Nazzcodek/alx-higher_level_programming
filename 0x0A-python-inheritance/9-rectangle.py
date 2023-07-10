#!/usr/bin/python3

"""
This is the module for Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a child class

    inheritance:
        it inherit from BaseGeometry
    """

    def __init__(self, width, height):
        """
            Initialize the instance

            Params:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width

    """public instnace"""
    def area(self):
        return self.__height * self.__width

    """ sting function"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
