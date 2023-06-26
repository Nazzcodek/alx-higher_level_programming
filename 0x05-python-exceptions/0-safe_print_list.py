#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []
    counter = 0
    try:
        for i in my_list[:x]:
            if x > my_list.index(my_list[-1]):
                x = my_list.index(my_list[-1])
                new_list.append(i)
            else:
                new_list.append(i)
        for i in new_list:
            counter += 1
            print('{}'.format(i), end='',)
        print()
    except Exception as e:
        print("An error occurred:", str(e))
    return counter
