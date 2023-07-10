#!/usr/bin/python3

"""
This is the module for 101-add_attribute.py
"""


def add_attribute(obj, attr, value):
    """
    add_attribute function

    params:
        obj: object to add attribute to
        attr: attribute to be added
        value: value of the new attribute
    Raises:
        TypeError: can't add new attribute
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
