#!/usr/bin/python3
"""A function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Attempts to add attributes to an object
    Args:
        obj: object an attribute will be added to
        att: the name of the attribute to add to obj
        value: The value of the attribute
    Raises:
    TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cna't add new attribute")
    setattr(obj, att, value)
