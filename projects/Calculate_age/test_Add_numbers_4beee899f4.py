# Test generated by RoostGPT for test roost-test using AI Type Open AI and AI Model gpt-4

import unittest
from add import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_Add_numbers_4beee899f4(self):
        # Test case 1: Check with positive numbers
        self.assertEqual(add_numbers(3, 2), 5, "Should be 5")

        # Test case 2: Check with negative numbers
        self.assertEqual(add_numbers(-1, -3), -4, "Should be -4")

        # Test case 3: Check with positive and negative number
        self.assertEqual(add_numbers(5, -2), 3, "Should be 3")

        # Test case 4: Check with zero
        self.assertEqual(add_numbers(0, 5), 5, "Should be 5")

        # Test case 5: Check with large numbers
        self.assertEqual(add_numbers(1000000, 2000000), 3000000, "Should be 3000000")

if __name__ == '__main__':
    unittest.main()
