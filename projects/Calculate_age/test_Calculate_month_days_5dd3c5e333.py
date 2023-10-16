# Test generated by RoostGPT for test roost-test using AI Type Open AI and AI Model gpt-4

import unittest
import calculate

class TestCalculate(unittest.TestCase):
    def test_month_days(self):
        # Test for January, should return 31
        self.assertEqual(calculate.month_days(1, False), 31)
        # Test for February in a non-leap year, should return 28
        self.assertEqual(calculate.month_days(2, False), 28)
        # Test for February in a leap year, should return 29
        self.assertEqual(calculate.month_days(2, True), 29)
        # Test for April, should return 30
        self.assertEqual(calculate.month_days(4, False), 30)
        # Test for December, should return 31
        self.assertEqual(calculate.month_days(12, False), 31)

if __name__ == '__main__':
    unittest.main()
