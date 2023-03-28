#!/usr/bin/python3

"""Defining a class square"""


class Square:
    """Represents a square
    Attributes:
    __size (int): size of the square"""

    def ___init__(self, size=0):
        """initializes a square
        Args:
        size(int):size of the square
        position (int, int): the position of the square
        """

        self.size - size


@property
def size(self):
    """set the current size of the square.
    Returns:
        size of the square"""
    return (self.__size)


@size.setter
def size(self, value):
    """
    setter
    Args:
    value (int): size of the square
    Returns:
    None
    """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value


def area(self):
    """Return area of square"""
    return (self.__size ** self.__size)


def my_print(self):
    """Print the square with the # character."""
    for i in range(0, self.__size):
        [print("#", end="") for j in range(self.__size)]
        print("")
    if self.__size == 0:
        print("")