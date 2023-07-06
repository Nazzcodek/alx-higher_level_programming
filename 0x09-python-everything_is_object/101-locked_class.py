#!/usr/bin/python3

""" lock class module"""


class LockedClass:
    """
    This object is locked for any instance creation

    Accepted: only first_name object is accepted
    """
    __slots__ = ['first_name']
