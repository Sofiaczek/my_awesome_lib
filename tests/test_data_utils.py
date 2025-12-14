import unittest
from my_awesome_lib.data_utils import average, max_value


class TestDataUtils(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_max_value(self):
        self.assertEqual(max_value([1, 9, 3]), 9)