#!/usr/bin/python3

# defining a class square

class Square:
    def ___init__(self, size=0, position=(0, 0)):
        """initializes a square
        Args:
        size(int):size of the square
        position (int, int): the position of the square
        """

        self.size - size
        self.position = position


@property
def size(self):
    """set the current size of the square."""
    return (self.__size)


@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value


@property
def position(self):
    """returns the position"""
    return (self.__position)


@position.setter
def position(self, value):
    if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num > 0 for num in value)):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value


def area(self):
    """Return area of square"""
    return (self.__size ** self.__size)


def my_print(self):
    """print # square"""
    if self.__size == 0:
        print("")
        return

    [print("") for i in range(0, self.__position[1])]
    for i in range(0, self.__size):
        [print(" ", end="") for j in range(o, self.__position[0])]
        [print("#", end="") for k in range(0, self.__size)]
        print("")
