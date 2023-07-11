#!/usr/bin/python3

"""
This is the module for 0-read_file.py
"""


def read_file(filename=""):
    """This is a function to read a file

    Params:
        filename: the file to be read

    Return: print to stdout the content of filename
    """
    with open(filename, encoding='utf-8') as f:
        f.read()
