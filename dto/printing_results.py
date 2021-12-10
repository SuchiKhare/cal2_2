"""Class for all calculator operations"""


class Print:
    """Base class for operations such as Add, Subtract, Multiply, Divide etc"""

    # The __init__ method is a constructor and runs as soon as an
    # object of a Operation class is instantiated.
    def __init__(self, input1, input2, operation_name, result):
        """Parameterized Constructor convert to generic input parameters to float"""
        # instance attribute values of type tuple and is protected
        self.input1 = input1
        self.input2 = input2
        self.operation_name = operation_name
        self.result = result

    def get_input1(self):
        """get input 1"""
        return self.input1

    def get_input2(self):
        """get input2"""
        return self.input2

    def get_operation_name(self):
        """get operation name"""
        return self.operation_name

    def get_result(self):
        """get result of the operation"""
        return self.result
