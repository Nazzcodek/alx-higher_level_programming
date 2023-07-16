#!/usr/bin/python3

import unittest

from models.base import Base


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


if __name__ == "__main__":
    unittest.main()

