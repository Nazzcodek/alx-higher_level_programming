#!/usr/bin/python3

"""
This is a module for rectangle object
"""


class Rectangle:
    """
    Initializes the class instance with a size attribute.
    Args:
        width (int): The width of the instance.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ deleting an instance"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Gets the width of the instance.
        Returns:
            int: The width of the instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width of the rectangle.
        Parameters:
            value (int): The width of the rectangle.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Gets the width of the instance.
        Returns:
            int: The width of the instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the height of the rectangle.
        Parameters:
            value (int): The height of the rectangle.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    """
    public area attribute
    """
    def area(self):
        area = self.__width * self.__height
        return area

    """
    public perimeter attribute
    """
    def perimeter(self):
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter

    def __str__(self):
        """ string rectangle"""
        width = self.__width
        height = self.__height
        str_rec = ''
        if width == 0 or height == 0:
            str_rec
        else:
            str_rec = '{}{}'.format((print_symbol * width + '\n') * (height - 1),
                                    print_symbol * width)
        return str_rec

    def __repr__(self):
        """ string represenatation"""
        width = self.__width
        height = self.__height
        return f'Rectangle({width}, {height})'
