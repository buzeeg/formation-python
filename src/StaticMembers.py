from PySide6.QtCore import Signal, Slot, QObject


class Rational:
    trucator = 2

    def __init__(self):
        self.numerator = 0
        self.denominator = 1


class DemoClass(QObject):
    # super_signal = Signal(str)
    super_signal = Signal(str, name="super_signal2")

    def __init__(self):
        super().__init__()

    def do_signal(self):
        self.super_signal.emit("Hello")


@Slot(str, result=None)
def a_slot(message):
    print(message)


if __name__ == '__main__':
    obj = Rational()
    print(obj.numerator)
    print(obj.denominator)
    print(obj.trucator)
    print("Dict objet:", obj.__dict__)
    print("Dict class:", Rational.__dict__)

    obj2 = Rational()
    obj2.__class__.trucator = 12  # equivalent to : Rational.trucator = 12
    print(obj.trucator)
    print(obj2.trucator)
    print("Dict objet:", obj.__dict__)
    print("Dict objet2:", obj2.__dict__)
    print(obj)
    print(obj2)

    sc = DemoClass()
    sc.super_signal.connect(a_slot)  # Test super_signal
    sc.do_signal()
