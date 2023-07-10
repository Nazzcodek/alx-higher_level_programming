#!/usr/bin/python3

"""
this is the module for the is_my_class function
"""


def is_same_class(obj, a_class):
    """
    is_my _class function

    Params:
        obj: object to look for instance
        a_class: class to lookup

    Return:
        boolean: True or False
    """
    return True if type(obj) == a_class else False
