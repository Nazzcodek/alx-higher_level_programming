#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = []
    for name in dir(hidden_4):
        if not name.startswith('__'):
            names.append(name)
    names.sort()
    for name in names:
        print(name)
