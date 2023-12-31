import pytest
from unittest.mock import Mock
from pytest_mock import mocker


from src.beverage_machine import CoffeeMachine


@pytest.fixture
def coffee_machine():
    full_machine = CoffeeMachine()
    full_machine.refill_all_ingredients()
    return full_machine


def test_make_coffee_with_input(coffee_machine, mocker):
    mocker.patch('builtins.input', side_effect=["yes", "yes", "2"])
    result = coffee_machine.make_coffee()
    assert "coffee is now ready" in result


def test_make_tea_with_input(coffee_machine, mocker):
    mocker.patch('builtins.input', return_value="1")
    result = coffee_machine.make_tea()
    assert "tea is now ready" in result
