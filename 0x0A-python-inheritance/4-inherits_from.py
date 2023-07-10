#!/usr/bin/python3

"""
This is a module for inherit_from function
"""


def inherits_from(obj, a_class):
    """
    The inherits_from function

    Params:
        obj: object to check inheritance
        a_class: class object inherit from

    Return:
        boolean: True or False
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
