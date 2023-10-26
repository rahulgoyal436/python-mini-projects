# Test generated by RoostGPT for test roost-test using AI Type Azure Open AI and AI Model roost-gpt4-32k

# Import necessary module
from add import add_numbers
import unittest

class TestAddNumbers(unittest.TestCase):

    def test_Add_numbers_4beee899f4(self):
        # Test the addition of two positive numbers
        result = add_numbers(3, 2)
        self.assertEqual(result, 5, "The result of addition of 3 and 2 should be 5.")

    def test_Add_numbers_negative(self):
        # Test the addition of one positive and one negative number
        result = add_numbers(3, -2)
        self.assertEqual(result, 1, "The result of addition of 3 and -2 should be 1.")

    def test_Add_numbers_zero(self):
        # Test the addition of a number and zero
        result = add_numbers(5, 0)
        self.assertEqual(result, 5, "The result of addition of 5 and 0 should be 5.")

    def test_Add_numbers_float(self):
        # Test the addition of floats
        result = add_numbers(5.5, 4.5)
        self.assertEqual(result, 10, "The result of addition of 5.5 and 4.5 should be 10.")

if __name__ == '__main__':
    unittest.main()
