#!/usr/bin/python3

"""
This is the unittest  module for Base class
"""

import unittest

import json
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_init_with_id(self):
        """Test the __init__ method with an id."""
        base = Base(id=123)
        self.assertEqual(base.id, 123)

    def test_init_without_id(self):
        """Test the __init__ method without an id."""
        base = Base()
        self.assertEqual(base.id, 2)

    def test_id_property(self):
        """Test the id property."""
        base = Base()
        self.assertEqual(base.id, 1)
        base.id = 456
        self.assertEqual(base.id, 456)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        # Test with empty list
        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), '[]')

        # Test with list of dictionaries
        rectangles = [Rectangle(1, 2), Rectangle(3, 4)]
        expected_json = '''[
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
            {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}
        ]'''
        self.assertEqual(Base.to_json_string(rectangles), expected_json)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        # Test with empty list of objects
        empty_list = []
        Base.save_to_file(empty_list)
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
        os.remove("Base.json")

        # Test with non-empty list of objects
        rectangles = [Rectangle(1, 2), Rectangle(3, 4)]
        Base.save_to_file(rectangles)
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", "r") as file:
            content = file.read()
        expected_json = '''[
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
            {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}
        ]'''
        self.assertEqual(content, expected_json)
        os.remove("Base.json")

    def test_from_json_string(self):
        """Test the from_json_string method"""
        # Test with empty JSON string
        empty_json = "[]"
        self.assertEqual(Base.from_json_string(empty_json), [])

        # Test with non-empty JSON string
        json_string = '''[
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
            {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}
        ]'''
        expected_list = [
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
            {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}
        ]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_create(self):
        """Test the create method"""
        # Test creating Rectangle instance
        rectangle_dict = {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}
        rectangle = Base.create(**rectangle_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        # Test loading instances from file
        rectangle1 = Rectangle(1, 2)
        rectangle2 = Rectangle(3, 4)
        rectangles = [rectangle1, rectangle2]
        Base.save_to_file(rectangles)

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertEqual(loaded_rectangles[0].id, rectangle1.id)
        self.assertEqual(loaded_rectangles[0].width, rectangle1.width)
        self.assertEqual(loaded_rectangles[0].height, rectangle1.height)
        self.assertEqual(loaded_rectangles[0].x, rectangle1.x)
        self.assertEqual(loaded_rectangles[0].y, rectangle1.y)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[1].id, rectangle2.id)
        self.assertEqual(loaded_rectangles[1].width, rectangle2.width)
        self.assertEqual(loaded_rectangles[1].height, rectangle2.height)
        self.assertEqual(loaded_rectangles[1].x, rectangle2.x)
        self.assertEqual(loaded_rectangles[1].y, rectangle2.y)

        os.remove("Rectangle.json")
    
    def setUp(self):
        """Setting up the test for csv"""
        # Clear any existing CSV files
        self.remove_csv_files()

        # Create test instances
        self.rectangles = [
            Rectangle(1, 2, 3, 4, 5),
            Rectangle(6, 7, 8, 9, 10)
        ]
        self.squares = [
            Square(11, 12, 13, 14),
            Square(15, 16, 17, 18)
        ]

    def tearDown(self):
        """Tear down csv file"""
        # Remove created CSV files
        self.remove_csv_files()

    @staticmethod
    def remove_csv_files():
        """remove csv file"""
        # Remove any existing CSV files
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_save_to_file_csv(self):
        """Test save to CSV file"""
        # Save rectangles to file
        Rectangle.save_to_file_csv(self.rectangles)
        # Check if the file exists
        self.assertTrue(os.path.exists("Rectangle.csv"))

        # Save squares to file
        Square.save_to_file_csv(self.squares)
        # Check if the file exists
        self.assertTrue(os.path.exists("Square.csv"))

    def test_load_from_file_csv(self):
        """ Test load CSV file """
        # Save rectangles to file
        Rectangle.save_to_file_csv(self.rectangles)
        # Load rectangles from file
        loaded_rectangles = Rectangle.load_from_file_csv()
        # Check if the loaded rectangles match the original rectangles
        self.assertEqual(loaded_rectangles, self.rectangles)

        # Save squares to file
        Square.save_to_file_csv(self.squares)
        # Load squares from file
        loaded_squares = Square.load_from_file_csv()
        # Check if the loaded squares match the original squares
        self.assertEqual(loaded_squares, self.squares)

if __name__ == "__main__":
    unittest.main()
