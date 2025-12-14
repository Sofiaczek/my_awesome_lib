import unittest
from my_awesome_lib.math_tools import add, subtract, factorial

"Testy dla modułu math_tools"

class TestMathTools(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)