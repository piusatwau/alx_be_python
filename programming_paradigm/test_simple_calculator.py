import unittest
from simple_calculator import SimpleCalculator

class Calc_testor(unittest.TestCase):
    def test_add(self):
        result = add(4, 5)
        self.assertEqual(result, 9)
    def test_subtract(self):
        result = subtract(6, 5)
        self.assertEqual(result, 1)
    def test_divide(self):
        result = divide(4, 2)
        self.assertEqual(result, 2)
    def test_multiply(self):
        result = multiply(4, 5)
        self.assertEqual(result, 20)
        
if __name__ == "__main__":
    unittest.main()