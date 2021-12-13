"""Abstract class"""
from abc import abstractmethod, ABC


class Result(ABC):
    """result for all the operations"""

    # pylint: disable=too-few-public-methods
    @abstractmethod
    def get_output(self):
        """this is the abstract method to be implemented by impl classes"""
