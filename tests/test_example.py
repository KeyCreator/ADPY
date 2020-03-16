import unittest
import requests


class TestExamples(unittest.TestCase):
    def test_zero_divizion(self):
        self.assertRaises(ZeroDivisionError, lambda : 2 / 0)


class TestExamples2(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.runner()
