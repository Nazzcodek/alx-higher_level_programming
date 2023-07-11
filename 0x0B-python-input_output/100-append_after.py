#!/usr/bin/python3

"""
this is the module for 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This fuction takes a filename and insert new_string after
    search_string

    params:
        filename: the file to insert to
        search_string: string to search for
        new_string: string to insert after search string
    Return:
        a new file that contains new contents
    """
    new_text = ''

    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(new_text)
