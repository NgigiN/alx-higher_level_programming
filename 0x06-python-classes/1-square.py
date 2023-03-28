#!/usr/bin/python3

# creating my class square
class Square:
    # instantiating it with the size as private
    def __init__(self, size):
        """Initializing a square
        Args:
        size : size of square as private"""
        self.__size = size
