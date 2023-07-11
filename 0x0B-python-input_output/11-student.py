#!/usr/bin/python3

"""
This is the module for 9-student.py
"""


class Student:
    """This is a student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initialization

        Params:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ public method"""
    def to_json(self, attrs=None):
        new_dict = {}

        if attrs or attrs == []:
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict

        else:
            return self.__dict__

    """ Public Method"""
    def reload_from_json(self, json):
        lst = list(self.__dict__.keys)
        for k, v in json.items():
            if k in lst:
                self.__setattr__(k, v)

