#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Represents a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
    Intializes an object rectangle
    """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the private attribute width
        """
        if not type(value) is int:
            raise TypeError("width must bbe an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the private attribute height
        """
        if not type(value) is int:
            raise TypeError("height must bbe an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter
        """
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        returns a representation of the rectangle
        """
        s = []
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                [s.append(str(self.print_symbol)) for j in range(self.__width)]
                if i != self.__height - 1:
                    s.append("\n")
        return ("".join(s))

    def __repr__(self):
        """returns a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        indicates deletion of rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the rectangle with a greater area
        """

        if type(rect_1) is Rectangle:
            TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is Rectangle:
            TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
