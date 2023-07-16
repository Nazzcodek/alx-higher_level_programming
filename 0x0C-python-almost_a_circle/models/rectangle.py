#!/usr/bin/python3

"""
This is the module for Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle object"""

    # constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of rectangle object
        params:
            width: width of the rectangle object
            height: height of the rectangle object
            x and y: cordinates of the rectangle object
            id: id of the object inherit from Base model
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def value_validator(attribute_name, value):
        """Validation function to check the type and value of the attribute"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if attribute_name == "height" or attribute_name == "width":
            if value <= 0:
                raise ValueError(f"{attribute_name} must be > 0")
        if attribute_name == 'y' or attribute_name == 'x':
            if value < 0:
                raise ValueError(f"{attribute_name} must be >= 0")

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the width of the rectangle.
        Params:
            value (int): The width of the rectangle.
        """
        Rectangle.value_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the height of the rectangle.
        Params:
            value (int): The height of the rectangle.
        """
        Rectangle.value_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ get the cordinate x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the cordinate x for the rectangle
        Params:
            value (int/float): x can only be positive or 0
        """
        Rectangle.value_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """ get the cordinate y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute
        Params:
            value (int): The new value for y
        """
        Rectangle.value_validator("y", value)
        self.__y = value

    """Public Method Area"""
    def area(self):
        """
        This method calculate the area of the rectangle
        using the width and height instance
        """
        width = self.__width
        height = self.__height
        area = width * height
        return area

    """Public Method Display"""
    def display(self):
        """
        Display the rectangle using '#'
        """
        width = self.__width
        height = self.__height
        for i in range(self.__y):
            print()
        for i in range(height):
            print(' ' * self.__x + '#' * width)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        w = self.__width
        h = self.__height
        d = self.id
        x = self.__x
        y = self.__y
        return f"""[Rectangle] ({d}) {x}/{y} - {w}/{h}"""

    """Public method Update"""
    def update(self, *args, **kwargs):
        """
        Updates the instance attributes of the Rectangle class.
        Args:
            *args: Variable-length argument list 
                   containing the values to update the attributes.
                   The order of the arguments should be: 
                   id, width, height, x, y.
            **kwargs: key value pair indicating which attribute
                      to update
        """
        attribute_names = ('id', 'width', 'height', 'x', 'y')

        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)

        for key, value in kwargs.items():
            if key in attribute_names:
                setattr(self, key, value)
