# Test generated by RoostGPT for test roost-test using AI Type Open AI and AI Model gpt-4

import unittest
from add import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers_positive(self):
        self.assertEqual(add_numbers(1, 2), 3, "Should be 3")

    def test_add_numbers_negative(self):
        self.assertEqual(add_numbers(-1, -1), -2, "Should be -2")

    def test_add_numbers_zero(self):
        self.assertEqual(add_numbers(0, 0), 0, "Should be 0")

    def test_add_numbers_float(self):
        self.assertEqual(add_numbers(1.5, 2.5), 4.0, "Should be 4.0")

    def test_add_numbers_mixed(self):
        self.assertEqual(add_numbers(-1, 2), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()
