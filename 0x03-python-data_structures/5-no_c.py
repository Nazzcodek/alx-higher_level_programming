#!/usr/bin/pthon3

def no_c(my_string):
    str = 'cC'
    for i in str:
        my_string = my_string.replace(i, '')
    return my_string
