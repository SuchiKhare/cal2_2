"""read file type of external file"""
import os
import pandas as pd


class Reader:
    """File reader class"""

    def __init__(self, file_name):
        """parameterized constructor"""
        self._file_name = file_name

    def read_file(self):
        """Method to process data from csv file to df"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/test_data", self._file_name)
        df_data = pd.read_csv(file_path, header=1, names=["input1", "input2", "result"])
        return df_data
