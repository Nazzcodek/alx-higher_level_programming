#!/usr/bin/python3
from sys import argv

result = 0
if __name__ == "__main__":
    for i in range(1, len(argv)):
        result += int(argv[i])
    print(result)
