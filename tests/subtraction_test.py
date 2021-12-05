"""Testing of Addition"""
from calc.calculations.subtraction import Subtraction


def test_calculation_subtraction():
    """test subtraction of numbers"""
    # Arrange
    my_num = (2.5, 3.0)
    # Act
    subtraction = Subtraction(my_num)
    # Assert
    output = subtraction.get_output()
    assert output == 5.5
