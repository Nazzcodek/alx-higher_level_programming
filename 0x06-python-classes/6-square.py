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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            ValueError: If `size` is less than zero.
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Gets the position of the instance
        Returns:
            int: The cordinates of the instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the sposition of the square.
        Parameters:
            value (tuple): the cordinates of the square.
        Raise:
            TypeError: if `value` is not an integer
        """
        if isinstance(value, tuple) \
                and len(value) == 2 \
                and all(isinstance(item, int) \
                and item > 0 for item in value):
                    self.__position = value
        else:
            error = "positon must be a tuple of 2 positive integers"
            raise TypeError(error)
    """
    public attribute area
    """
    def area(self):
        return self.__size ** 2

    """
    public attribute my_print
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
