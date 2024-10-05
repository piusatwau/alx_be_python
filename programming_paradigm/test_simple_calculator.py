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

# test_simple_calculator.py

# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)

        # Testing division by zero
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)  # This should raise ValueError
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == "__main__":
    unittest.main()

