#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) >= 65:
            upper += chr(ord(i) - 32)
        return upper
