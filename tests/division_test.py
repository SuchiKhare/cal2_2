"""Testing of Addition"""
import pytest

from calc.calculations.division import Division


def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    # Arrange
    my_numbers = (3.0, 1.0, 1.5)
    division = Division(my_numbers)
    # Act
    # Assert
    assert division.get_output() == "0.22"
    with pytest.raises(ZeroDivisionError):
        output = Division((1.0, 0.0, 1.0))
        assert output.get_output() == 1.0
