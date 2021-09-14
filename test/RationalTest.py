import unittest

from Rational import Rational


class MyTestCase(unittest.TestCase):
    def test_add(self):
        r1: Rational = Rational(1, 3)
        r2: Rational = Rational(2, 1)
        res: Rational = r1 + r2
        self.assertEqual(7, res.n)
        self.assertEqual(3, res.d)

    def test_simplify(self):
        r = Rational(35, 10)
        r.simplify()
        self.assertEqual(7, r.n)
        self.assertEqual(2, r.d)

    @unittest.expectedFailure
    def test_bad_denominator1(self):
        Rational(1, 0)

    def test_bad_denominator2(self):
        with self.assertRaises(ValueError):
            Rational(1, 0)

        with self.assertRaises(TypeError):
            Rational("toto", 1)

    def test_dead(self):
        # raise Exception("erreur")
        pass


if __name__ == '__main__':
    unittest.main()
