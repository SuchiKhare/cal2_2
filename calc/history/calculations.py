"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction


class Calculations:
    """Manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get total items in history list"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get object of last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get result of last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_output()

    @staticmethod
    def get_first_calculation_object():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_first_calculation_result_value():
        """get result of first calculation"""
        calculation = Calculations.get_first_calculation_object()
        return calculation.get_output()

    @staticmethod
    def get_calculation(num):
        """ get a calculation at particular index of history list"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(operation):
        """ add calculation to history"""
        return Calculations.history.append(operation)

    @staticmethod
    def add_addition_calculation(tuple_elements):
        """Add addition object to history"""
        addition = Addition.create_operation(tuple_elements)
        Calculations.add_calculation(addition)
        return True

    @staticmethod
    def add_subtraction_calculation(tuple_elements):
        """Add subtraction object to history"""
        subtract = Subtraction.create_operation(tuple_elements)
        Calculations.add_calculation(subtract)
        return True

    @staticmethod
    def add_multiplication_calculation(tuple_elements):
        """Add multiplication object to history"""
        multiply = Multiplication.create_operation(tuple_elements)
        Calculations.add_calculation(multiply)
        return True

    @staticmethod
    def add_division_calculation(tuple_elements):
        """Add division object to history"""
        divide = Division.create_operation(tuple_elements)
        Calculations.add_calculation(divide)
        return True
