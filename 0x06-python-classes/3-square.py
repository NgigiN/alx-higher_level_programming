#!/usr/bin/python3

"""Defining a class square"""


class Square:
    """Represents a square
    Attributes:
    __size (int): size of the square"""

    def __init__(self, size=0):
        """Initializes a square
                Args:
                size (int): new size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the square's area
        Returns the area of the square"""
        return (self.__size * self.__size)
