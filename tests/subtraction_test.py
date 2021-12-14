"""Testing Subtraction"""
import logging
from calc.calculations.subtraction import Subtraction
from calc.utils.file_reader import Reader

logger = logging.getLogger(__name__)


def test_calculation_subtraction():
    """test subtraction"""
    file_name = "subtraction.csv"
    data_frame = Reader(file_name).read_file()
    for ind, row in data_frame.iterrows():
        tuple_values = (row.input1, row.input2)
        subtraction = Subtraction.create_operation(tuple_values)
        result = subtraction.get_output()
        logger.info("%s  - %s - %s = %s", ind, row.input1, row.input2, result)
        assert result == data_frame['result'][ind]
