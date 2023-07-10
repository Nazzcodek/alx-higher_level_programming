#!/usr/bin/python3

"""
This is the module for the child class MyList
"""


class MyList(list):
    """
    This is the child class MyList

    Inherit:
        from list module
    """
    def print_sorted(self):
        """
        This is the print_sorted function
        """
        print(sorted(self))
