#!/usr/bin/python3
"""integer adding function"""


def add_integer(a, b=98):
    """Returns sum of a and b

    Floats are typecasted to integers before addition

    Raises:
    TypeError: if either is a non-integer or non-float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)

    return a + b
