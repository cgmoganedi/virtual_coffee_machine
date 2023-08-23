import pytest
from src.beverage_machine import CoffeeMachine

@pytest.fixture
def ingredient_manager():
    coffee_machine = CoffeeMachine()
    return coffee_machine.ingredient_manager

def test_get_ingredient(ingredient_manager):
    ingredient = ingredient_manager.get_ingredient("water")
    assert ingredient.name == "water"

def test_refill_ingredient(ingredient_manager):
    ingredient_manager.refill_ingredient("water")
    ingredient = ingredient_manager.get_ingredient("water")
    quantity = ingredient.quantity
    max_capacity = ingredient.max_capacity
    print('ABV', quantity, max_capacity)
    assert quantity == max_capacity
