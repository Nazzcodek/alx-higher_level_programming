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

    """Public method Update"""
    def update(self, *args, **kwargs):
        """
        Updates the instance attributes of the Square class.
        Args:
            *args: Variable-length argument list
                   containing the values to update the attributes.
                   The order of the arguments should be:
                   id, size, x, y.
            **kwargs: key value pair indicating which attribute
                      to update
        """
        attribute_names = ('id', 'size', 'x', 'y')

        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)

        for key, value in kwargs.items():
            if key in attribute_names:
                setattr(self, key, value)
