#!/usr/bin/python3
"""
this is function defination file 6-peak.py
"""


def find_peak(list_of_integers):
    """
    Method that find the peak of a list
    Param:
        list_of_integers
    Return: peak of list
    """
    size = len(list_of_integers)

    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    mid = size // 2
    peak = list_of_integers[mid]

    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
       (mid == size - 1 or peak >= list_of_integers[mid + 1]):
        return peak

    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
