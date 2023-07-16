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

if __name__ == "__main__":
    unittest.main()
