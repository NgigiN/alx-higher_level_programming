#!/usr/bin/python3
"""
Defines an empty Rectangle class
"""


class Rectangle:
    """
    Representation of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        getter for the private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private width
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width nust be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not type(value) is int:
            raise TypeError("height nust be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
