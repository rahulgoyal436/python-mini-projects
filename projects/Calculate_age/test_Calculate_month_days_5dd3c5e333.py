import unittest
import calculate

class TestCalculate(unittest.TestCase):

    def test_valid_month_not_leap_year(self):
        self.assertEqual(calculate.month_days(1, False), 31)

    def test_valid_month_leap_year(self):
        self.assertEqual(calculate.month_days(1, True), 31)

    def test_february_not_leap_year(self):
        self.assertEqual(calculate.month_days(2, False), 28)

    def test_february_leap_year(self):
        self.assertEqual(calculate.month_days(2, True), 29)

    def test_30_days_month(self):
        self.assertEqual(calculate.month_days(4, True), 30)

    def test_invalid_month(self):
        self.assertIsNone(calculate.month_days(13, True))

    def test_invalid_month_non_integer(self):
        with self.assertRaises(TypeError):
            calculate.month_days("February", True)

    def test_non_boolean_leap_year(self):
        with self.assertRaises(TypeError):
            calculate.month_days(1, 'yes')

if __name__ == '__main__':
    unittest.main(verbosity=3)
