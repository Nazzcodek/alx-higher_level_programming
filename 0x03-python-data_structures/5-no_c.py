#!/usr/bin/pthon3

def no_c(my_string):
    str = 'cC'
    new_str = ''
    for i in my_string:
        if i not in str:
            new_str += i
    return new_str
