"""Write external file"""


class Write:
    # pylint: disable=too-few-public-methods

    """Writer Class"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_csv_file(to_file, df):
        """Write CSV from pandas dataframe"""
        df.to_csv(to_file, encoding='utf-8')
