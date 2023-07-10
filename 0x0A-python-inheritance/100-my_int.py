#!/usr/bin/python3

"""
This is the module for MyInt class
"""


class MyInt(int):
    """
    This is MyInt object
    Inheretance:
        int(): Inherit from int method
    """

    """private instance"""
    def __eq__(self, other):
        return super().__ne__(other)

    """private instance"""
    def __ne__(self, other):
        return super().__eq__(other)
