import pytest
from beverage_machine import CoffeeMachine

@pytest.fixture
def coffee_machine(session, ingredient_manager):
    return CoffeeMachine(session, ingredient_manager)

def test_coffee_machine_make_coffee(coffee_machine, mocker):
    mocker.patch('builtins.input', side_effect=["yes", "yes", "2"])
    result = coffee_machine.make_coffee()
    assert "Enjoy your coffee!" in result
    # Check if ingredient levels are correctly updated
    ingredient = coffee_machine.ingredient_manager.get_ingredient("water")
    assert ingredient.quantity == ingredient.max_capacity

# Similar tests for make_tea
