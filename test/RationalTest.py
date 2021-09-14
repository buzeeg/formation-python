import unittest

from Rational import Rational


class MyTestCase(unittest.TestCase):
    def test_something(self):
        Rational.simplify()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
