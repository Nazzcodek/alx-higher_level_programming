#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = sum(map(lambda x: x[0] * x[1], my_list))
    b = sum(map(lambda x: x[1], my_list))
    average = a / b
    return average
