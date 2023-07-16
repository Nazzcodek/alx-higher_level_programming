#!/usr/bin/python3

"""This is the test module for Square class"""

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """ This is the test object for square"""

    def test_string_representation(self):
        """
        Test the string representation of the Square.
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5/5")

    def test_update_id(self):
        """
        Test the update method of the Square with the id argument.
        """
        square = Square(5, 2, 3, 1)
        square.update(id=10)
        self.assertEqual(square.id, 10)

    def test_update_size(self):
        """
        Test the update method of the Square with the size argument.
        """
        square = Square(5, 2, 3, 1)
        square.update(width=7)
        self.assertEqual(square.width, 7)

    def test_update_x(self):
        """
        Test the update method of the Square with the x argument.
        """
        square = Square(5, 2, 3, 1)
        square.update(x=8)
        self.assertEqual(square.x, 8)

    def test_update_y(self):
        """
        Test the update method of the Square with the y argument.
        """
        square = Square(5, 2, 3, 1)
        square.update(y=9)
        self.assertEqual(square.y, 9)

    def test_update_multiple_args(self):
        """
        Test the update method of the Square with multiple arguments.
        """
        square = Square(5, 2, 3, 1)
        square.update(10, height=7, y=9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.y, 9)


if __name__ == '__main__':
    unittest.main()
