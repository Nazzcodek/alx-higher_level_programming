#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary

    key_del = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            key_del.append(k)

    for i in key_del:
        del a_dictionary[i]

    return a_dictionary
