#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in new_list:
        if i < 0:
            i = -i
        modulo = i % 2
        if modulo == 0:
            new_list.append(True)
        else:
            new_list.appen(False)
    return new_list
