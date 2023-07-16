#!/usr/bin/python3

"""
This is the module for square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square object """

    # Constructor
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the sqaure object
        Params:
            size: size of the sqaure
            x: x cordinate
            y: y cordinate
            id: id of the sqaure instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String reprsentation of square"""
        s1 = self.width
        s2 = self.height
        x = self.x
        y = self.y
        d = self.id
        return f"[Square] ({d}) {x}/{y} - {s1}/{s2}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size using
            width and height of rectangle class
            and equate them to a value:
        """
        self.width = value
        self.height = value
