#!/usr/bin/python3
"""Class int inheriting from data type int"""


class MyInt(int):
    def __new__(clss, *args, **anotherargs):
        """Creating an instance of the class"""
        return super(Myint, clss).__new__(clss, *args, **anotherargs)

    def __eq__(self, other):
        """This should change != to =="""
        return int(self) != other

    def __ne__(self, other):
        """this should change == to !="""
        return int(self) == other
