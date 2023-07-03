#!/usr/bin/python3

"""
This is the module for say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    The say_my_name function
    Params:
        first_name: First name of the user
        last_name: Last name of the user

    Raise:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    print:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        error_msg = ""
        if not isinstance(first_name, str):
            error_msg += "first_name must be a string"
        if not isinstance(last_name, str):
            if error_msg:
                error_msg += " and "
            error_msg += "last_name must be a string"
        raise TypeError(error_msg)

    print(f"My name is {first_name} {last_name}")
