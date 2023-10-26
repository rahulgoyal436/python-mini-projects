# Test generated by RoostGPT for test roost-test using AI Type Azure Open AI and AI Model roost-gpt4-32k

import unittest
from add import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_Add_numbers_4beee899f4(self):
        # Test case 1: Check the sum of two positive integers
        num1 = 2  # TODO: Change these values to test with other numbers
        num2 = 3  # TODO: Change these values to test with other numbers
        result = add_numbers(num1, num2)
        self.assertEqual(result, 5, f"Expected Result : 5, Received Result : {result}")

        # Test case 2: Check the sum of a positive and a negative integer
        num1 = -2  # TODO: Change these values to test with other numbers
        num2 = 5   # TODO: Change these values to test with other numbers
        result = add_numbers(num1, num2)
        self.assertEqual(result, 3, f"Expected Result : 3, Received Result : {result}")

        # Test case 3: Check the sum of two negative integers
        num1 = -2  # TODO: Change these values to test with other numbers
        num2 = -3  # TODO: Change these values to test with other numbers
        result = add_numbers(num1, num2)
        self.assertEqual(result, -5, f"Expected Result : -5, Received Result : {result}")

        # Test case 4: Check the sum of zero and an integer
        num1 = 0  # TODO: Change these values to test with other numbers
        num2 = 5  # TODO: Change these values to test with other numbers
        result = add_numbers(num1, num2)
        self.assertEqual(result, 5, f"Expected Result : 5, Received Result : {result}")

if __name__ == '__main__':
    unittest.main()
