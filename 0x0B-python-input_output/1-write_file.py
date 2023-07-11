#!/usr/bin/python3

"""
This is the module for 1-write_file.py
"""


def write_file(filename="", text=""):
    """
    This function write content to a file

    Params:
        filename: file to create or write to
        text: text to write to filename

    Return: content of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = f.writ(text)
        return content
