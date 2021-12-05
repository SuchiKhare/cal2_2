"""Testing of Addition"""
from calc.calculations.multiplication import Multiplication


def test_calculation_multiplication():
    """test multiplication of numbers"""
    # Arrange
    my_num = (2.5, -3.0, 2.0)
    # Act
    multiply = Multiplication(my_num)
    # Assert
    output = multiply.get_output()
    assert output == -15.0
