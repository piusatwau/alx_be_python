# Writing Unit Tests
# Python provides a built-in module called unittest for writing unit tests. Let’s explore its basic functionalities:

# Test Cases:
# We define individual tests as test cases within a TestCase class. Each test case has a specific method named with test_ 
# followed by a descriptive name. Inside this method, we write code to:

# Set up the test environment (e.g., create objects, initialize data).
# Execute the code we want to test (e.g., call the function with specific inputs).
# Assert the expected outcome using self.assertEqual(actual, expected)

# Test Runners:
# Once you’ve written your test cases, you need a test runner to execute them. The unittest module provides a TextTestRunner 
# class that can be used to run all test cases within a test suite.


import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_positives(self):
        result = add(5, 3)
        self.assertEqual(result, 8)
        
    def test_add_negatives(self):
        result = add(5, -3)
        self.assertEqual(result, 2)
if __name__ == "__main__":
    unittest.main()
