import pytest
from unittest.mock import Mock
from pytest_mock import mocker


from src.beverage_machine import CoffeeMachine


@pytest.fixture
def coffee_machine():
    full_machine = CoffeeMachine()
    full_machine.refill_all_ingredients()
    return full_machine


def test_coffee_machine_make_coffee(coffee_machine, mocker):
    mocker.patch('builtins.input', side_effect=["yes", "yes", "2"])
    ingredient = coffee_machine.ingredient_manager.get_ingredient("water")
    initial_quantity_water = ingredient.quantity
    
    ingredient = coffee_machine.ingredient_manager.get_ingredient("milk")
    initial_quantity_milk = ingredient.quantity
    
    ingredient = coffee_machine.ingredient_manager.get_ingredient("coffee_beans")
    initial_quantity_beans = ingredient.quantity
    
    coffee_water_cost = 150
    coffee_milk_cost = 50
    coffee_beans_cost = 10
    
    result = coffee_machine.make_coffee()
    assert "coffee is now ready" in result
    # Check if ingredient levels are correctly updated
    ingredient = coffee_machine.ingredient_manager.get_ingredient("water")
    assert ingredient.quantity == initial_quantity_water - coffee_water_cost
    
    ingredient = coffee_machine.ingredient_manager.get_ingredient("milk")
    assert ingredient.quantity == initial_quantity_milk - coffee_milk_cost
    
    ingredient = coffee_machine.ingredient_manager.get_ingredient("coffee_beans")
    assert ingredient.quantity == initial_quantity_beans - coffee_beans_cost

# Similar tests for make_tea
