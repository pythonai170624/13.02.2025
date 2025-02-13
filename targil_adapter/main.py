from targil_adapter.adapter_float_int import AdapterFloat2Int
from targil_adapter.factorial_calc import FactorialCalculator


def print_factorial_number(factorial, number):
    print(factorial.calc_factorial(number))

if __name__ == "__main__":

    # 1*2*3*4*5 = 120
    print_factorial_number(FactorialCalculator(), 5)
    # print_factorial_number(FactorialCalculator(), 3.0) # Error
    print_factorial_number(AdapterFloat2Int(), 3.0)

