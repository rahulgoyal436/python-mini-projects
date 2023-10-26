# Test generated by RoostGPT for test roost-test using AI Type Azure Open AI and AI Model roost-gpt4-32k

import unittest
from unittest.mock import patch
from calculate import month_days

class MonthDaysTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_month_days(self):
        # test normal months
        self.assertEqual(month_days(1, True), 31)
        self.assertEqual(month_days(3, True), 31)
        self.assertEqual(month_days(5, True), 31)
        self.assertEqual(month_days(7, True), 31)
        self.assertEqual(month_days(8, True), 31)
        self.assertEqual(month_days(10, True), 31)
        self.assertEqual(month_days(12, True), 31)

        self.assertEqual(month_days(4, True), 30)
        self.assertEqual(month_days(6, True), 30)
        self.assertEqual(month_days(9, True), 30)
        self.assertEqual(month_days(11, True), 30)

        # test February on leap year
        self.assertEqual(month_days(2, True), 29)

        # test February on non-leap year
        self.assertEqual(month_days(2, False), 28)

if __name__ == "__main__":
    unittest.main(verbosity=2)
