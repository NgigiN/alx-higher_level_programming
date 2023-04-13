#!/usr/bin/pyhton3
"""A Student Class"""


class Student:
    """A Student blueprint"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representationof a Student instance
        Args:
                attrs: is a list of strings, only attribute names contained in this
                list must be retrieved otherwise all attributes must be retrieved"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
