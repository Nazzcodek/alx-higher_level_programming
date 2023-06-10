#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = 0
    if len(my_list) == 0:
        return None
    else:
        max_num = sorted(my_list)[-1]
    return max_num
