"""Testing Division"""
import logging
import pytest
from calc.calculations.division import Division
from calc.utils.file_reader import Reader

logger = logging.getLogger(__name__)


def test_calculation_division():
    """test multiplication"""
    file_name = "division.csv"
    data_frame = Reader(file_name).read_file()
    for ind, row in data_frame.iterrows():
        tuple_values = (row.input1, row.input2)
        division = Division.create_operation(tuple_values)
        try:
            result = division.get_output()
            logger.info("%s  - %s / %s = %s", ind, row.input1, row.input2, result)
            assert division.get_output() == data_frame['result'][ind].round(decimals=3)
        except ZeroDivisionError:
            logger.error("%s %s Divide by zero error", ind, file_name)
            with pytest.raises(ZeroDivisionError):
                assert division.get_output() is True
