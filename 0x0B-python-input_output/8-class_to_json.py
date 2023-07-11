#!/usr/bin/python3

"""
this is the module for 8-claass_to_json.py
"""


def class_to_json(obj):
    """ this function turn a class object to json
    Params:
        obj: class object
    """
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    elif isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]

    elif isinstance(obj, (str, int, bool)):
        return obj

    elif obj is None:
        return None

    else:
        attributes = {}
        for attr in dir(obj):
            if not attr.startswith('__') and not callable(getattr(obj, attr)):
                attributes[attr] = class_to_json(getattr(obj, attr))
        return attributes
