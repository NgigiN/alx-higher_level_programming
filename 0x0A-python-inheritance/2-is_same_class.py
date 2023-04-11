#!/usr/bin/python3
"""
This module is for checking if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Return True if object is instance of the class, otherwise
    false
    """
    return (type(obj) == a_class)
