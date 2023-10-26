# Test generated by RoostGPT for test roost-test using AI Type Azure Open AI and AI Model roost-gpt4-32k

import calculate
import unittest

class TestCalculate(unittest.TestCase):

    def test_month_days(self):
        # Test for a month that should return 31 days
        self.assertEqual(calculate.month_days(1, True), 31)

        # Test for a month that should return 30 days
        self.assertEqual(calculate.month_days(4, True), 30)

        # Test for February in a leap year
        self.assertEqual(calculate.month_days(2, True), 29)

        # Test for February in a non-leap year
        self.assertEqual(calculate.month_days(2, False), 28)

# Run the unit test
if __name__ == "__main__":
    unittest.main(verbosity=2)
