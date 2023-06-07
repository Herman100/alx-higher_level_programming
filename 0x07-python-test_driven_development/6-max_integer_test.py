#!/usr/bin/python3
"""
Unittests for the max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function
    """

    def test_max_integer(self):
        """
        Test the max_integer function with various inputs
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
