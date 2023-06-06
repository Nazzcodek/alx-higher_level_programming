#!/usr/bin/python3
reverse = ""
for i in range(25, -1, -1):
    reverse += chr(i + 97)
    if i % 2 == 0:
        reverse = reverse[:-1] + chr(ord(reverse[-1]) - 32)

print("{}".format(reverse), end='')
