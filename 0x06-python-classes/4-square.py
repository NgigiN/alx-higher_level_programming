#!/usr/bin/python3

# creating a class square
class Square:
    def __init__(self, size=0):
        """Initialize a new square.
         Args:
             size (int): The size of the new square.
         """
        self.size = size

    @property
    def size(self):
        """set the size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return self.__size ** 2
