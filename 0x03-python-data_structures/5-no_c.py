#!/usr/bin/python3

def no_c(my_string):
    rm_str = 'cC'
    new_str = ''
    for i in my_string:
        if i not in rm_str:
            new_str += i
    return new_str
