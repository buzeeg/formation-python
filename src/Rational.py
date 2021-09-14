from __future__ import annotations
import math


class Rational(object):

    # Constructor
    def __init__(self, num: int = 0, den: int = 1):
        self.n = num
        self.d = den

    # Property definition 1
    def get_n(self):
        return self.__n

    def set_n(self, num):
        if not isinstance(num, int):
            raise TypeError("Numerator must be an int")
        self.__n = num

    n = property(get_n, set_n)

    # Property definition 2
    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, den):
        if not isinstance(den, int):
            raise TypeError("Denominateur must be an int")
        if den == 0:
            raise ValueError("Denominator must not be 0")
        self.__d = den

    # Custom display
    def __str__(self):
        return f"[{self.__n}/{self.__d}]"

    # Custom add
    def __add__(self, other: Rational):
        return Rational(
            self.n * other.d + self.d * other.n,
            self.d * other.d
        )

    def simplify(self):
        divisor = math.gcd(self.n, self.d)
        # To prevent float result
        self.n //= divisor
        self.d //= divisor


# POO tests
r1 = Rational(0, 1)
print(r1)
r1.n = 12
r1.d = 5
print(r1)
# r1._Rational__d = 2
print(r1)
# print(r1.__dict__)

# Typing tests
r2 = Rational(den=4)
print(r2)
r3: Rational = Rational(1, 3)
r4: Rational = Rational(2, 1)
res: Rational = r3 + r4
print(res)
# dir(list)
# dir(date)
print(res.__dict__)

toSimplify = Rational(256, 8)
toSimplify.simplify()
print(toSimplify)
