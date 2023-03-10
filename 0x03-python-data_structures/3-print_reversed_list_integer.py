#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    list_len = len(my_list) - 1
    i = 0
    while i <= list_len:
        print("{}".format(my_list[i]))
        i += 1
