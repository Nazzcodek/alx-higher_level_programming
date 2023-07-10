#!/usr/bin/python3

"""
This is the module for the lookup function
"""


def lookup(obj):
    """
    This is the lookup function

    Params:
        obj: object to lookup
    Return:
        list of all method of obj
    """
    return dir(obj)
