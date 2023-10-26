# Test generated by RoostGPT for test roost-test using AI Type Azure Open AI and AI Model roost-gpt4-32k

import unittest
from unittest.mock import patch
import calculate
from calendar import isleap

class TestCalculate(unittest.TestCase):
    def test_judge_leap_year(self):
        leap_year = 2000
        non_leap_year = 2001

        # Test when the year is a leap year
        result = calculate.judge_leap_year(leap_year)
        self.assertEqual(result, isleap(leap_year))

        # Test when the year is not a leap year
        result = calculate.judge_leap_year(non_leap_year)
        self.assertEqual(result, isleap(non_leap_year))

if __name__ == "__main__":
    unittest.main(verbosity=2)
