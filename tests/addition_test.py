"""Testing of Addition"""
from calc.calculations.addition import Addition


def test_calculation_addition():
    """test addition of numbers"""
    # Arrange
    my_num = (2.5, 3.0)
    # Act
    addition = Addition(my_num)
    # Assert
    output = addition.get_output()
    assert output == 5.5
