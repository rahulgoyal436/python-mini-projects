# Test generated by RoostGPT for test roost-test using AI Type Open AI and AI Model gpt-4

import unittest
from calculate import judge_leap_year

class TestCalculate(unittest.TestCase):
    def test_judge_leap_year(self):
        self.assertEqual(judge_leap_year(2000), True)
        self.assertEqual(judge_leap_year(1900), False)
        self.assertEqual(judge_leap_year(2004), True)
        self.assertEqual(judge_leap_year(2001), False)

if __name__ == '__main__':
    unittest.main()
