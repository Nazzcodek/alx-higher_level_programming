#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    new_t = []

    for i in range(2):
        add = a[i] + b[i]
        new_t.append(add)
    return tuple(new_t)
