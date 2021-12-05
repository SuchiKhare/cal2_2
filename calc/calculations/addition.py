"""Class for Addition Operation"""
from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Addition(Operation, Result):
    """subclass Addition extending base Operation"""

    # This is the instance method
    def get_output(self):
        """Adds the elements in tuple and return"""
        sum_of_elements = 0.0
        for value in self._values:
            sum_of_elements = sum_of_elements + value
        return sum_of_elements
