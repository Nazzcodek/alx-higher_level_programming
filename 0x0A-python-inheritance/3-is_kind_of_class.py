#!/usr/bin/python3

"""
This is the modeule for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    This is is_kind_of_class function

    Params:
        obj: object to look for class instance
        a_class: class the object is an instance of

    Return:
        boolean: True or False
    """
    return True if isinstance(obj, a_class) else False
