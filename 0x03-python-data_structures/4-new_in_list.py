#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    new_list = my_list[:]
    if idx < 0:
        return (new_list)
    elif idx > list_len:
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
