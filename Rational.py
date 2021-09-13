class Rational(object):

    # Constructor
    def __init__(self, num, den):
        self.__n = num
        if den != 0:
            self.__d = den
        else:
            self.__d = 1
            raise ZeroDivisionError

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


# Tests
r1 = Rational(0, 1)
print(r1)
r1.n = 12
r1.d = 5
print(r1)
r1._Rational__d = 2
print(r1)
# print(r1.__dict__)
