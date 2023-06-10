#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse = []
    if len(my_list) == 0:
        reverse == my_list
    else:
        reverse = my_list[::-1]
    for i in reverse:
        print("{:d}".format(i))
