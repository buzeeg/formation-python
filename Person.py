class Person:
    def __init__(self, first: str = "john", last: str = "DOE"):
        self.first_name = first
        self.last_name = last

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if value is None or len(value) < 1:
            raise ValueError("First name must be given")
        self.__first_name = value.lower()

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        if value is None or len(value) < 1:
            raise ValueError("Last name must be given")
        self.__last_name = value.upper()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


###
# Employee class definition
###
class Employee(Person):
    SMIC: float = 1_500.0

    def __init__(self, first: str = "john", last: str = "DOE", salary: float = SMIC):
        super().__init__(first, last)
        self.salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        if not isinstance(value, int) and \
           not isinstance(value, float):
            raise TypeError("Salary must be a number")
        if value < Employee.SMIC:
            raise ValueError("Salary too low")
        self.__salary = float(value)

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.salary:.2f} €)"


if __name__ == '__main__':
    tests = [
        Person("Dark", "Vador"),
        Person("D", "Vador"),
        Person("Dark", "V"),
        Person("None", "Vador"),
        Person("Dark", "None"),
        Person(),
        Employee("Dark", "Vador"),
        Employee("Dark", "Vador", 2000),
        Employee("Dark", "Vador", 10000),
    ]
    for p in tests:
        print(p)

    print(isinstance(tests[6], object))
    print(isinstance(tests[6], Person))
    print(isinstance(tests[6], Employee))
    print(isinstance(tests[6], str))
    print(isinstance(tests[2], Person))
    print(isinstance(tests[2], Employee))
