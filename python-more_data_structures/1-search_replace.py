#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = [replace if x==search else x for x in new_list]
    return new_list
