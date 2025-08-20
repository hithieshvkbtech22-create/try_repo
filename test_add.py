# test_add.py

import unittest
from add_two_numbers import add_two_numbers  # we'll make a function in your main file

class TestAddition(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_two_numbers(2, 3), 5)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
