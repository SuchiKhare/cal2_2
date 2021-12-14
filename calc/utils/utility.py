"""utility method overall"""
from dto.printing_results import Print


class Utility:
    """Overall utility class"""

    @staticmethod
    def convert_df_dto(df_data):
        """Method to convert dataframe to DTO object"""
        print_lst = []
        for ind in df_data.index:
            print("to be tuple", df_data['input1'][ind], df_data['input2'][ind], df_data['operation_name'][ind], df_data['result'][ind])
            input1 = df_data['input1'][ind]
            input2 = df_data['input2'][ind]
            operation = df_data['operation_name'][ind]
            my_output = df_data['result'][ind]
            print_dto = Print(input1, input2, operation, my_output)
            print_lst.append(print_dto)
        return print_lst
