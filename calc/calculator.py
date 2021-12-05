"""Main Calculator"""
from calc.history.calculations import Calculations


# This class just call the methods to calculate
class Calculator:
    """calculator class"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def addition(tuple_elements: tuple):
        """adds elements in tuple"""
        Calculations.add_addition_calculation(tuple_elements)
        return True

    @staticmethod
    def subtraction(tuple_elements: tuple):
        """subtract elements in tuple"""
        Calculations.add_subtraction_calculation(tuple_elements)
        return True

    @staticmethod
    def multiplication(tuple_elements: tuple):
        """multiply elements in tuple"""
        Calculations.add_multiplication_calculation(tuple_elements)
        return True

    @staticmethod
    def division(tuple_elements: tuple):
        """divide elements in tuple"""
        Calculations.add_division_calculation(tuple_elements)
        return True

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()
