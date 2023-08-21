import pytest
from beverage_machine import IngredientManager

@pytest.fixture
def ingredient_manager(session):
    return IngredientManager(session)

def test_get_ingredient(ingredient_manager):
    ingredient = ingredient_manager.get_ingredient("water")
    assert ingredient.name == "water"

def test_refill_ingredient(ingredient_manager):
    ingredient_manager.refill_ingredient("water")
    ingredient = ingredient_manager.get_ingredient("water")
    assert ingredient.quantity == ingredient.max_capacity
