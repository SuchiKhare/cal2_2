"""Class for Division Operation"""
from abc import ABC

from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Division(Operation, Result, ABC):
    """subclass Division extending base Operation"""

    # This is the instance method
    def get_output(self):
        """get the division results"""
        try:
            for ind, value in enumerate(self._values):
                if ind == 0:
                    div_of_elements = value
                else:
                    div_of_elements = div_of_elements / value
            my_formatter = "{0:.2f}"
            return my_formatter.format(div_of_elements)
        except ZeroDivisionError:
            return 'ZeroDivisionError'
