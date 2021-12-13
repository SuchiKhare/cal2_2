"""Testing pandas class"""
from calc.utils.file_reader import Reader


def test_pandas_read_file():
    """Testing the file type check"""


def test_read_file():
    """Testing df creation after extracting data from csv file"""
    file_name = "addition.csv"
    df_test_csv_data = Reader(file_name).read_file()
    assert df_test_csv_data is not None
