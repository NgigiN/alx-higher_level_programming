#!/usr/bin/python3
"""
This module returns the list of available attributs and methods of
an object
"""


def lookup(obj):
    """
    the dir function returns a list of all available attributes and methods of an object
    Args:
    obj: the object to be evaluated

    Return:
    A list of variables
    """
    return (dir(obj))
