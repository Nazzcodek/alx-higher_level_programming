#!/usr/bin/python3
from sys import argv
count = len(argv) - 1

if __name__ == "__main__":
    if count == 0:
        print(f'{count} arguments.')
    elif count == 1:
        print(f'{count} argument:')
        print(f"1: {argv[1]}")
    else:
        print(f'{count} arguments:')
        for i in range(1, count + 1):
            print(f"{i}: {argv[i]}")
