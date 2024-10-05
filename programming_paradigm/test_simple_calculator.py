# import unittest
# from simple_calculator import SimpleCalculator

# class Calc_testor(unittest.TestCase):
#     def test_add(self):
#         result = add(4, 5)
#         self.assertEqual(result, 9)
#     def test_subtract(self):
#         result = subtract(6, 5)
#         self.assertEqual(result, 1)
#     def test_divide(self):
#         result = divide(4, 2)
#         self.assertEqual(result, 2)
#     def test_multiply(self):
#         result = multiply(4, 5)
#         self.assertEqual(result, 20)
        
# if __name__ == "__main__":
#     unittest.main()

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, 5), -4)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(6, 0))
        self.assertIsNone(self.calc.divide(-6, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
