#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_at_end(self):
        """Test a list where the max value is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test a list where the max value is in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_with_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_same(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([8, 8, 8, 8]), 8)

    def test_mixed_positive_negative(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-12, -2, 5, 3, -9]), 5)

    def test_floats(self):
        """Test a list with float values"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_inf(self):
        """Test a list with infinite values"""
        self.assertEqual(max_integer([11, float('inf'), 33, 44]), float('inf'))

    def test_nan(self):
        """Test a list with NaN values"""
        self.assertEqual(max_integer([11, float('NaN'), 33, 44]), 44)


if __name__ == '__main__':
    unittest.main()
