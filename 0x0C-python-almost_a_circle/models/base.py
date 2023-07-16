#!/usr/bin/python3

"""
This is the module for base.py
"""


class Base:
    """this is the Base object"""

    # private attribute
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):
        """
        Initialization
        Params:
            id: id of the base
        Return:
            id
        """
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects

    @property
    def id(self):
        """
        get the ID
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        set id value
        """
        self.__id = value
