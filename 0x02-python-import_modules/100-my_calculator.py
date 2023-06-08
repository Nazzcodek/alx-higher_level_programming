#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    operator = ['+', '-', '*', '/']

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]

    if sign not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if sign == '+':
            print(f"{a} {sign} {b} = {add(a, b)}")
        elif sign == '-':
            print(f"{a} {sign} {b} = {sub(a, b)}")
        elif sign == '*':
            print(f"{a} {sign} {b} = {mul(a, b)}")
        else:
            print(f"{a} {sign} {b} = {div(a, b)}")
