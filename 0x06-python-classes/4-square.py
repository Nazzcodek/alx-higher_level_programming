#!/usr/bin/python3

"""
This is a class Square
"""


class Square:
    """
    Initializes the class instance with a size attribute.
    Args:
        size (int): The size of the instance.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the instance.
        Returns:
            int: The size of the instance.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.
        Parameters:
            size (int): The size of the square.
        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than zero.i
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    """
    public area attribute
    """
    def area(self):
        return self.__size ** 2
