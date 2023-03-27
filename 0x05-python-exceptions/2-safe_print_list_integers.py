#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(item), end='')
            except (ValueError, TypeError):
                pass
    except (IndexError):
        print("not in the list")
