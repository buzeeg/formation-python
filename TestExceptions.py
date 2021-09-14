from random import randint
from traceback import print_exc


def function3():
    print("Begin function3")
    while True:
        try:
            value = randint(0, 2)
            print(1 / value)
            break
        except ZeroDivisionError as e:
            print("ZeroDivisionError : ")
            print(e)
        except BaseException as e:
            print("Unknown Error : ")
            print(e)
            print_exc()
        finally:
            print("finally always executed")
    print("End function3")


def function2():
    print("Begin function2")
    function3()
    print("End function2")


def function1():
    print("Begin function1")
    function2()
    print("End function1")


if __name__ == '__main__':
    print("Begin main")
    function1()
    print("End main")
