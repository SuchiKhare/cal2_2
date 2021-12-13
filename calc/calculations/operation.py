"""Class for all calculator operations"""


class Operation:
    """Base class for operations such as Add, Subtract, Multiply, Divide etc"""

    # The __init__ method is a constructor and runs as soon as an
    # object of a Operation class is instantiated.
    def __init__(self, values: tuple):
        """Parameterized Constructor convert to generic input parameters to float"""
        # instance attribute values of type tuple and is protected
        self._values = Operation.convert_cal_input_to_float(values)

    @staticmethod
    def convert_cal_input_to_float(values):
        """this function standardize to get all calculator inputs to float values"""
        # any given tuple will be converted to tuple of floats by iterating the tuple
        values_float_list = []
        for value in values:
            # typecasting to float
            values_float_list.append(float(value))
        return tuple(values_float_list)

    @classmethod
    def create_operation(cls, values: tuple):
        """design pattern - factory to create the instance at one place"""
        # cls keyword (ideal name) : we can only access the members of the class
        return cls(values)
