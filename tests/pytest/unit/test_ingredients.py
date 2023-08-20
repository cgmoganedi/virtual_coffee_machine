import pytest
from coffee_machine import IngredientManager

@pytest.fixture
def ingredient_manager(session):
    return IngredientManager(session)

def test_get_ingredient(ingredient_manager):
    ingredient = ingredient_manager.get_ingredient("water")
    assert ingredient.name == "water"

def test_refill_ingredient(ingredient_manager):
    ingredient_manager.refill_ingredient("water", 100)
    ingredient = ingredient_manager.get_ingredient("water")
    assert ingredient.quantity == 100

def test_refill_exceeds_max_capacity(ingredient_manager):
    with pytest.raises(ValueError):
        ingredient_manager.refill_ingredient("water", 1000)