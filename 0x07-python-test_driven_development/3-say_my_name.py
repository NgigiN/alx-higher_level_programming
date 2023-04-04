#!/usr/bin/python3
"""a function to print the first and last name"""


def say_my_name(first_name, last_name=""):
    """Prints a statements with the first and last name variables

    if either first name or last name is not string an error is raised

    Raises:
    TypeError: if either is not an integer"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
