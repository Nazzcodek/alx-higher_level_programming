#!/usr/bin/python3

"""
This is the module for 5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function write object in json to filename

    Params:
        my_obj: JSON object to write to file
        filename: file to write to

    Return:
        JSON OBJECT in filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = json.loads(my_obj)
        save = f.write(content)
        return save
