"""Read external file"""
from pathlib import Path

import pandas as pd


class Reader:
    # pylint: disable=too-few-public-methods

    """Reader Class"""

    def __init__(self, file_name):
        """"""
        self._file_name = file_name

    def abs_path(filepath):
        relative = Path(filepath)
        return relative.absolute()

    # pylint: disable=too-few-public-methods
    def read_csv_file(self):
        """Read CSV into pandas dataframe"""
        file_df = pd.read_csv(self._file_name, header=None, error_bad_lines=False, index_col=False)
        return file_df.iloc[1:, 1:]  # to drop result and header
