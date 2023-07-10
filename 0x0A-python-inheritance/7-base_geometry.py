#!/usr/bin/python3

"""
this is the module for the BaseGeomety class
"""


class BaseGeometry:
    """ this is the base geomerty class """

    """ public instance"""
    def area(self):
        raise Exception("area() is not implemented")

    """ public instance 
        Params:
            name: name of the instance variable
            value: name value

        Rises:
            TypeError: name must be an int
            ValuError: name must be greater than 0
    """
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
