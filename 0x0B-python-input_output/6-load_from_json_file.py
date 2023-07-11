#!/usr/bin/python3

"""
This is the module for 6-load_from_json_file.py
"""

import json


def load_from_json_file(filename):
    """
    This function load from json

    Params:
        filename: the file to load

    Return:
        loaded JSOn file
    """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        load = json.loads(content)
        return load
