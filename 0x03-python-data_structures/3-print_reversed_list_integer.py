#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        reverse = my_list[::-1]
        for i in reverse:
            print("{:d}".format(i))
