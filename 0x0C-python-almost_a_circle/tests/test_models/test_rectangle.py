#!/sur/bin/python

import unittest
import sys
import io

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_init(self):
        """Test the __init__ method."""
        rectangle = Rectangle(10, 20, 0, 0)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_width_setter(self):
        """Test the width setter."""
        rectangle = Rectangle(10, 20, 0, 0)
        rectangle.width = 50
        self.assertEqual(rectangle.width, 50)

    def test_height_setter(self):
        """Test the height setter."""
        rectangle = Rectangle(10, 20, 0, 0)
        rectangle.height = 100
        self.assertEqual(rectangle.height, 100)

    def test_x_setter(self):
        """Test the x setter."""
        rectangle = Rectangle(10, 20, 0, 0)
        rectangle.x = 100
        self.assertEqual(rectangle.x, 100)

    def test_y_setter(self):
        """Test the y setter."""
        rectangle = Rectangle(10, 20, 0, 0)
        rectangle.y = 50
        self.assertEqual(rectangle.y, 50)

    def test_value_validator(self):
        """Test the value_validator function."""
        with self.assertRaises(TypeError):
            Rectangle.value_validator("width", "hello")

        with self.assertRaises(ValueError):
            Rectangle.value_validator("width", -10)

        with self.assertRaises(ValueError):
            Rectangle.value_validator("height", 0)

        with self.assertRaises(ValueError):
            Rectangle.value_validator("x", -10)

        with self.assertRaises(ValueError):
            Rectangle.value_validator("y", -10)

    def test_display(self):
        """ Test display method"""
        rect = Rectangle(4, 6)
        expected_output = '####\n####\n####\n####\n####\n####\n'
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        # Get the captured output and reset the standard output
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Print the expected and captured output for visual comparison
        print("Expected Output:")
        print(expected_output)
        print("Captured Output:")
        print(output)
        # Compare the expected and captured output visually
        self.assertEqual(expected_output, output)

    def test_str(self):
        """Test the __str__ method."""
        rectangle = Rectangle(10, 20, 5, 5, 1)
        expected_output = "[Rectangle] (1) 5/5 - 10/20"
        self.assertEqual(str(rectangle), expected_output)

    def test_update_with_args(self):
        """Test the update method."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_update_with_kwargs(self):
        """Test the Update methode using kwargs"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(id=1, width=6, height=7, y=8)

        print(rectangle.id)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 8)

    def test_update_with_args_and_kwargs(self):
        """Test the Update method using both args and kwargs"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, y=8)

        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 8)

    def test_update_with_no_args_or_kwargs(self):
        """
        Test the Update method with no args or kwargs
        """
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update()

        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method to return a dictionary of the square.
        """
        rectangle = Rectangle(10, 2, 1, 9)
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
