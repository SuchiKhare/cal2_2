import os
import shutil
import logging

from calc.calculator import Calculator
from calc.history.calculations_csv import CalculationsCSV
from calc.utils.file_reader import Reader
from tests.addition_test import test_calculation_addition
from tests.division_test import test_calculation_division
from tests.multiplication_test import test_calculation_multiplication
from tests.subtraction_test import test_calculation_subtraction

import pathlib

BASE_DIR = pathlib.Path().resolve()

input_path = os.path.join(BASE_DIR, "tests", "test_data")
results_path = os.path.join(BASE_DIR, "tests", "log")
output_file_path = os.path.join(BASE_DIR, "tests", "done_files")

logging.basicConfig(
    filename=os.path.join(results_path, "my_log.log"),
    filemode='a',
    # format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    # datefmt='%s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def process_files(file_path):
    for file_name in os.listdir(file_path):

        input_file_full_path = os.path.join(file_path, file_name)
        print(f"Processing the File {file_name}")
        my_df = Reader(file_name).read_file()
        if "addition" in file_name:
            test_calculation_addition(my_df)
        elif "subtraction" in file_name:
            test_calculation_subtraction(my_df)
        elif "multiplication" in file_name:
            test_calculation_multiplication(my_df)
        elif "division" in file_name:
            test_calculation_division(my_df, file_name)
        '''
        data = {
            'result': ['0'],
            'input1': ['100'],
            'input2': ['200'],
            'operation_name': ['subtraction']
        }
        Calculator.write_history_to_csv(data)
        ret_data = Calculator.get_history_from_csv()
        print("ret_data \n", ret_data)
        '''

        shutil.move(input_file_full_path, output_file_path)
        print("yay !! processing is done")


if __name__ == "__main__":
    process_files(input_path)
