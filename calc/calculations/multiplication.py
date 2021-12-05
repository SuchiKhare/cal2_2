"""Class for Addition Operation"""
from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Multiplication(Operation, Result):
    """subclass Multiplication extending base Operation"""

    # This is the instance method
    def get_output(self):
        """Multiplies the elements in tuple and return"""
        multiply_of_elements = 1.0
        for value in self._values:
            multiply_of_elements = multiply_of_elements * value
        return multiply_of_elements
