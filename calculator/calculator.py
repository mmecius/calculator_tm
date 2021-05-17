import itertools
import pytest
import doctest
from hypothesis import given, assume, strategies as st


class Calculator:
    def __init__(self, number1: float, number2: float):
        self.__number1 = number1
        self.__number2 = number2
        self.result = 0

    def set_number1(self, number1):
        """Set number1"""
        return self.__number1 == number1

    def get_number1(self):
        """Get number1"""
        return self.__number1

    def set_number2(self, number2):
        """Set number1"""
        return self.__number2 == number2

    def get_number2(self):
        """Get number2"""
        return self.__number2

    def addition(self):
        """Adds two numbers
         number1 + number2 = result
        For example:
        >>> calc_test = Calculator(3,2)
        >>> calc_test.addition()
        5.0
        """
        try:
            self.result = self.__number1 + self.__number2
        except TypeError:
            print("Must be number, not a string")
        return float(self.result)

    def subtraction(self):
        """Subtracts number2 from number1
        number1 - number2 = result

        For example:
        >>> calc_test = Calculator(3,2)
        >>> calc_test.subtraction()
        1.0
        """
        try:
            self.result = self.__number1 - self.__number2
        except TypeError:
            print("Must be number, not a string")
        return float(self.result)

    def multiplication(self):
        """Multiply two numbers
        number1 * number2 = result

        For example:
        >>> calc_test = Calculator(3,2)
        >>> calc_test.multiplication()
        6.0
        """
        try:
            self.result = self.__number1 * self.__number2
        except TypeError:
            print("Must be number, not a string")
        return float(self.result)

    def division(self):
        """Divides number1 by number2
        number1 / number2 = result

        For example:
        >>> calc_test = Calculator(6,2)
        >>> calc_test.division()
        3.0
        """
        try:
            self.result = self.__number1 / self.__number2
        except ZeroDivisionError:
            return 0.0
        except TypeError:
            print("Must be number, not a string")
        return float(self.result)

    def root_of_number(self):
        """Takes root number2 of numbers1
        For example:
        >>> calc_test = Calculator(4,2)
        >>> calc_test.root_of_number()
        2.0
        """
        try:
            self.result = self.__number1 ** (1 / float(self.__number2))
        except TypeError:
            print("Must be number, not a string")
        except ZeroDivisionError:
            return 0.0
        return self.result

    def reset_result(self):
        """Reset result to zero"""
        self.result = 0
        return self.result


# Tests


def test_addition():
    calc_test = Calculator(3, 3)
    assert calc_test.addition() == 6.0


def test_subtraction():
    calc_test = Calculator(4, 3)
    assert calc_test.subtraction() == 1.0


def test_multiplication():
    calc_test = Calculator(3, 2)
    assert calc_test.multiplication() == 6.0


def test_division():
    calc_test = Calculator(6, 2)
    assert calc_test.division() == 3.0


def test_root_of_number():
    calc_test = Calculator(4, 2)
    assert calc_test.root_of_number() == 2.0


def test_types():
    with pytest.raises(TypeError):
        Calculator("a", 1)
        Calculator.addition()
        Calculator.subtraction()
        Calculator.multiplication()
        Calculator.division()
        Calculator.root_of_number()


def torture_test():
    args = [10, 11, 2, 0.5, -1.3, 99]
    for t in itertools.permutations(args, 2):
        if t == 0:
            with pytest.raises(ZeroDivisionError):
                calc_testing = Calculator(*t)
                calc_testing.addition()
                calc_testing.subtraction()
                calc_testing.multiplication()
                calc_testing.division()
                calc_testing.root_of_number()
        else:
            calc_testing = Calculator(*t)
            calc_testing.addition()
            calc_testing.subtraction()
            calc_testing.multiplication()
            calc_testing.division()
            calc_testing.root_of_number()


@given(
    a=st.floats(min_value=-10000, max_value=10000),
    b=st.floats(min_value=-10000, max_value=10000),
)
def test_calculator(a, b):
    calc_test = Calculator(a, b)
    assert calc_test.addition() == a + b
    assert calc_test.subtraction() == a - b
    assert calc_test.multiplication() == a * b
    if a == 0.0 or b == 0.0:
        assert calc_test.division() == 0.0
    else:
        assert calc_test.division() == a / b
    if a == 0.0 or b == 0.0:
        assert calc_test.root_of_number() == 0.0
    else:
        assert calc_test.root_of_number() == a ** (1 / float(b))


test_addition()
test_subtraction()
test_multiplication()
test_division()
test_root_of_number()
test_types()
torture_test()
doctest.testmod()
test_calculator()
