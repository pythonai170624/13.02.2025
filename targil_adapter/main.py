import math

from targil_adapter.adapter_float_int import AdapterFloat2Int
from targil_adapter.data_holder import DataHolder
from targil_adapter.factorial_calc import FactorialCalculator


def print_factorial_number(factorial, number):
    print(factorial.calc_factorial(number))

if __name__ == "__main__":

    print_factorial_number(FactorialCalculator(), 5)

    print_factorial_number(AdapterFloat2Int(), 3.5555)
