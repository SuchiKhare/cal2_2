"""Class for Subtraction Operation"""
from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Subtraction(Operation, Result):
    """subclass Subtraction extending base Operation"""

    # This is the instance method
    def get_output(self):
        """Subtract the elements in tuple and return"""
        diff = 0.0
        for ind, value in enumerate(self._values):
            if ind == 0:
                diff = value
            else:
                diff = diff - value
        return diff
