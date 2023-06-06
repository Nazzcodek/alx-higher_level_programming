#!/usr/bin/python3
for i in range(10):
    for n in range(i + 1, 10):
        if i * 10 + n < 89:
            print("{:02d}".format(i * 10 + n), end=', ')

print("{:02d}".format(89), end='')
print()
            

