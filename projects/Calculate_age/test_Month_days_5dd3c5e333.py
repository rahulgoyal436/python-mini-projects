# Test generated by RoostGPT for test roost-test using AI Type Open AI and AI Model gpt-4

import unittest
from calendar import isleap
from calculate import month_days

class TestMonthDays(unittest.TestCase):

    def test_Month_days_5dd3c5e333(self):
        # Test case 1: Leap year, February
        self.assertEqual(month_days(2, isleap(2020)), 29, "Failed: It's a leap year, February should have 29 days")

        # Test case 2: Non-Leap year, February
        self.assertEqual(month_days(2, isleap(2021)), 28, "Failed: It's not a leap year, February should have 28 days")
        
        # Test case 3: Month with 31 days
        self.assertEqual(month_days(1, isleap(2020)), 31, "Failed: January should have 31 days")
        
        # Test case 4: Month with 30 days
        self.assertEqual(month_days(4, isleap(2020)), 30, "Failed: April should have 30 days")

        # Test case 5: Invalid month
        with self.assertRaises(TypeError):
            month_days(13, isleap(2020))

        # Test case 6: Invalid leap_year input
        with self.assertRaises(TypeError):
            month_days(2, '2020')

if __name__ == "__main__":
    unittest.main()
