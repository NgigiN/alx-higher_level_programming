#!/usr/bin/python3
"""
Module to checks if object is inherited or not
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class or is inherited (directly or indirectlye)
    Args:
    obj: the object to check
    a_class: the class to check against.

    Return:
    True if the object is an instance or False if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
