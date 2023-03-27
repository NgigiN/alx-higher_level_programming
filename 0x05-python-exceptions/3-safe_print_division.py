#!/usr/bin/python3

def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except (ZeroDivisionError):
        print("not so fast")
        return None
    finally:
        print("{}".format(c), end='')
        return c
