#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for item in my_list[:x]:
            print("{}".format(my_list[x]), end='')
    except:
        print("not in the list")
