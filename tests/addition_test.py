"""Testing Addition"""
import logging
from calc.calculations.addition import Addition
from calc.utils.file_reader import Reader

logger = logging.getLogger(__name__)


def test_calculation_addition():
    """Test addition"""
    file_name = "addition.csv"
    data_frame = Reader(file_name).read_file()
    for ind, row in data_frame.iterrows():
        tuple_values = (row.input1, row.input2)
        addition = Addition.create_operation(tuple_values)
        result = addition.get_output()
        logger.info("%s  - %s + %s = %s", ind, row.input1, row.input2, result)
        assert result == row.result
