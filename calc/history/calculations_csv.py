"""Calculation history Class"""
import os
import pandas as pd
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction


class CalculationsCSV:
    """Manages the history of calculations"""

    # The __init__ method is a constructor and runs as soon as an
    # object of an Operation class is instantiated.
    def __init__(self, file_name):
        """Parameterized Constructor"""
        self.file_name = file_name

    @staticmethod
    def create(op_name, tuple_values):
        """create instance"""
        operation = ""
        if op_name == "addition":
            operation = Addition.create_operation(tuple_values)
        elif op_name == "subtraction":
            operation = Subtraction.create_operation(tuple_values)
        elif op_name == "division":
            operation = Division.create_operation(tuple_values)
        elif op_name == "multiplication":
            operation = Multiplication.create_operation(tuple_values)
        return operation

    @staticmethod
    def get_history():
        """get history"""
        df_data = CalculationsCSV.read_history_from_csv()
        print("get_history = ", str(df_data))
        for ind in df_data.index:
            print("to be tuple", df_data['input1'][ind], df_data['input2'][ind], df_data['operation_name'][ind])
            tuple_values = (df_data['input1'][ind], df_data['input2'][ind])
            operation = CalculationsCSV.create(df_data["operation_name"][ind], tuple_values)
            df_data.iat[ind, df_data.columns.get_loc('result')] = operation.get_output()
        return df_data

    @staticmethod
    def read_history_from_csv():
        """Read the history from csv """
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/file/", "history.csv")
        df_data = pd.read_csv(file_path, header=None, names=["result", "input1", "input2", "operation_name"],
                              delimiter=',')
        return df_data

    @staticmethod
    def write_history_to_csv(data_frame):
        """Write the history to csv file"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/file/", "history.csv")
        data_frame = pd.DataFrame(data_frame)
        data_frame.to_csv(file_path, mode='a', header=None, index=None)

    @staticmethod
    def get_history_details():
        """get history details"""
        count = CalculationsCSV.count_history()
        first_operation = CalculationsCSV.get_first_calculation_object()
        first_result = CalculationsCSV.get_first_calculation_result_value()
        last_operation = CalculationsCSV.get_last_calculation_object()
        last_result = CalculationsCSV.get_last_calculation_result_value()
        return str(count), str(first_operation), str(first_result), str(last_operation), str(last_result)

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/file/", "history.csv")
        pd.DataFrame().to_csv(file_path, mode='w', header=None, index=None)
        return True

    @staticmethod
    def count_history():
        """get total items in history list"""
        return len(CalculationsCSV.read_history_from_csv())

    @staticmethod
    def get_last_calculation_object():
        """get object of last calculation"""
        df_data = CalculationsCSV.read_history_from_csv()
        length = len(df_data)
        operation_name = df_data["operation_name"][length - 1]
        return operation_name

    @staticmethod
    def get_last_calculation_result_value():
        """get result value of last cal"""
        df_data = CalculationsCSV.read_history_from_csv()
        length = len(df_data)
        operation_name = df_data["operation_name"][length - 1]
        tuple_values = (df_data['input1'][length - 1], df_data['input2'][length - 1])
        operation = CalculationsCSV.create(operation_name, tuple_values)
        result = operation.get_output()
        return result

    @staticmethod
    def get_first_calculation_object():
        """get first calculation"""
        df_data = CalculationsCSV.read_history_from_csv()
        operation_name = df_data["operation_name"][0]
        return operation_name

    @staticmethod
    def get_first_calculation_result_value():
        """get result value of first cal"""
        df_data = CalculationsCSV.read_history_from_csv()
        operation_name = df_data["operation_name"][0]
        tuple_values = (df_data['input1'][0], df_data['input2'][0])
        operation = CalculationsCSV.create(operation_name, tuple_values)
        result = operation.get_output()
        return result

    @staticmethod
    def get_calculation(num):
        """ get a calculation at particular index of history list"""
        operation_name = "Not Valid"
        df_data = CalculationsCSV.read_history_from_csv()
        for ind in df_data.index:
            if ind == num:
                operation_name = df_data["operation_name"][num]
        return operation_name
