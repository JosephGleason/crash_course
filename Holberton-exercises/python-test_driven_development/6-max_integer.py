#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([-1, 2, 0, 1]), 2)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
