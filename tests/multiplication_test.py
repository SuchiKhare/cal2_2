"""Testing Multiplication"""
import logging
from calc.calculations.multiplication import Multiplication
from calc.utils.file_reader import Reader

logger = logging.getLogger(__name__)


def test_calculation_multiplication():
    """test multiplication"""
    file_name = "multiplication.csv"
    data_frame = Reader(file_name).read_file()
    for ind, row in data_frame.iterrows():
        tuple_values = (row.input1, row.input2)
        multiplication = Multiplication.create_operation(tuple_values)
        result = multiplication.get_output()
        logger.info("%s  - %s * %s = %s", ind, row.input1, row.input2, result)
        assert result == data_frame['result'][ind]
