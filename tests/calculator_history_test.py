"""Testing the Calculator History"""
import pytest

from calc.calculations.multiplication import Multiplication
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition


@pytest.fixture
def clear_history_fixture():
    """fixture method will run each time passed to the test"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def setup_calculation_fixture():
    """fixture method will run each time passed to the test"""
    # pylint: disable=redefined-outer-name
    values = (2, 1)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    values2 = (1, 1)
    addition2 = Addition(values2)
    Calculations.add_calculation(addition2)
    values3 = (1, 4)
    multiplication1 = Multiplication(values3)
    Calculations.add_calculation(multiplication1)


def test_add_calculation_to_history(clear_history_fixture, setup_calculation_fixture):
    """testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 3


def test_clear_calculation_history(clear_history_fixture, setup_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 3
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True


def test_get_calculation(clear_history_fixture, setup_calculation_fixture):
    """testing calculation at particular index of history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_output() == 3


def test_get_calc_last_result_value(clear_history_fixture, setup_calculation_fixture):
    """testing get the last calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 4


def test_get_calculation_first_object(clear_history_fixture, setup_calculation_fixture):
    """testing get the first calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation_object().get_output() == 3


def test_get_calculation_first_result(clear_history_fixture, setup_calculation_fixture):
    """testing get the first calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation_result_value() == 3


def test_history_count(clear_history_fixture, setup_calculation_fixture):
    """Testing get the total count of calculations in history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 3


def test_get_calc_last_result_object(clear_history_fixture, setup_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(Calculations.get_last_calculation_object(), Multiplication)
