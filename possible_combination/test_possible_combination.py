#!/usr/bin/python3

import unittest

comb = __import__('possible_combination').combination

class TestCombination(unittest.TestCase):
    """ This class provides all possible test cases for the combination function."""

    # Let's test the function for valid inputs

    def test_no_pet(self):
        self.assertEqual(comb(0), 0)
    def test_one_pet(self):
        self.assertEqual(comb(1), 1)
    def test_two_pet(self):
        self.assertEqual(comb(2), 2)
    def test_three_pet(self):
        self.assertEqual(comb(3), 3)
    def test_four_pet(self):
        self.assertEqual(comb(4), 5)
    def test_six_pet(self):
        self.assertEqual(comb(6), 13)
    def test_ten_pet(self):
        self.assertEqual(comb(10), 89)
    def test_twenty_pet(self):
        self.assertEqual(comb(20), 10946)

    # Let's test the function for non-integer inputs

    def test_list_input(self):
        with self.assertRaisesRegex(TypeError, "The Number of pets must be integer!"):
            result = comb([1, 2, 3 ])
    def test_tuple_input(self):
        with self.assertRaisesRegex(TypeError, "The Number of pets must be integer!"):
            result = comb((1, ))
    def test_string_input(self):
        with self.assertRaisesRegex(TypeError, "The Number of pets must be integer!"):
            result = comb('test me')
    def test_float_input(self):
        with self.assertRaisesRegex(TypeError, "The Number of pets must be integer!"):
            result = comb(34.89)
    def test_dict_input(self):
        with self.assertRaisesRegex(TypeError, "The Number of pets must be integer!"):
            result = comb({'key': 'value1', 'key2': 23})

    # Let's test the function for negative inputs

    def test_negative1_input(self):
        with self.assertRaisesRegex(ValueError, "The Number of pets can't be negative"):
            result = comb(-2)
    def test_negative2_input(self):
        with self.assertRaisesRegex(ValueError, "The Number of pets can't be negative"):
            result = comb(-345)

    # Let's test for in appropriate arguments including no and extra arguments.

    def test_with_no_input(self):
        with self.assertRaises(TypeError):
            result = comb()
    def test_with_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            result = comb(1, 2, 3)
