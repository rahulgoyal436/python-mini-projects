import unittest
from calculate import month_days

class TestCalculate(unittest.TestCase):

    def test_month_days_31_leap_year(self):
        self.assertEqual(month_days(1, True), 31)
        self.assertEqual(month_days(3, True), 31)
        self.assertEqual(month_days(5, True), 31)
        
    def test_month_days_31(self):
        self.assertEqual(month_days(1, False), 31)
        self.assertEqual(month_days(3, False), 31)
        self.assertEqual(month_days(5, False), 31)

    def test_month_days_30_leap_year(self):
        self.assertEqual(month_days(4, True), 30)
        self.assertEqual(month_days(6, True), 30)
        self.assertEqual(month_days(9, True), 30)

    def test_month_days_30(self):
        self.assertEqual(month_days(4, False), 30)
        self.assertEqual(month_days(6, False), 30)
        self.assertEqual(month_days(9, False), 30)

    def test_month_days_29(self):
        self.assertEqual(month_days(2, True), 29)
    
    def test_month_days_28(self):
        self.assertEqual(month_days(2, False), 28)
        
    def test_invalid_month(self):
        self.assertIsNone(month_days(13, False))
        self.assertIsNone(month_days(-1, False))
        self.assertIsNone(month_days(5000, False))

    def test_invalid_leap_year(self):
        self.assertIsNone(month_days(2, "abc"))
        self.assertIsNone(month_days(2, None))
    
    def test_invalid_month_type(self):
        self.assertIsNone(month_days("february", True))
        self.assertIsNone(month_days(None, True))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            month_days()
    
    def test_excessive_args(self):
        with self.assertRaises(TypeError):
            month_days(2, True, 15)

    def test_null_args(self):
        with self.assertRaises(TypeError):
            month_days(None, None)
    
    def test_string_args(self):
        with self.assertRaises(ValueError):
            month_days("2", "True")
            
    def test_special_char_args(self):
        with self.assertRaises(ValueError):
            month_days("$", "%")

if __name__ == '__main__':
    unittest.main(verbosity=2)
