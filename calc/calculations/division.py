"""Class for Division Operation"""
from abc import ABC

from calc.calculations.operation import Operation
from calc.calculations.result import Result


class Division(Operation, Result, ABC):
    """subclass Division extending base Operation"""

    # This is the instance method
    def get_output(self):
        """get the division results"""
        div_of_elements = 1.0
        try:
            for value in self._values:
                div_of_elements = div_of_elements / value
            my_formatter = "{0:.2f}"
            div_of_elements = my_formatter.format(div_of_elements)
        except ZeroDivisionError as my_err:
            raise ZeroDivisionError from my_err
        return div_of_elements
