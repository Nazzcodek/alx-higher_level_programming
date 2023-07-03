#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        numbers = [3, 6, 8, 20, 15]
        max_num = max_integer(numbers)
        self.assertEqual(max_num, 20)

    def test_negative_int(self):
        numbers = [-2, -20, -1, 0]
        max_num = max_integer(numbers)
        self.assertEqual(max_num, 0)

    def test_alphabet_ma(self):
        string = 'Naziff Bello'
        max_num = max_integer(string)
        self.assertEqual(max_num, 'z')

    def test_none(self):
        with self.assertRaises(TypeError):
            max_num = max_integer(None)
            max_num

    def test_types(self):
        with self.assertRaises(TypeError):
            max_num = max_integer(['Nazif', 10, True])
            max_num

    def test_list_string(self):
        str_list = ['Naziff', 'Bello', 'name', 'school']
        max_num = max_integer(str_list)
        self.assertEqual(max_num, 'school')

    def test_empty_list(self):
        emp = []
        max_num = max_integer(emp)
        self.assertEqual(max_num, None)

    def test_dup(self):
        numbers = [-2, 2.0, 15, 15, 0]
        max_num = max_integer(numbers)
        self.assertEqual(max_num, 15)
