
from coffee_machine import IngredientManager
from models import Ingredient

def seed_ingredients(session):
    # Ingredient names and their initial quantities
    initial_ingredients = [
        {'name': 'water', 'max_capacity': 750, 'quantity': 750, 'unit_of_measure': 'ml'},
        {'name': 'coffee_beans', 'max_capacity': 250, 'quantity': 250, 'unit_of_measure': 'grams'},
        {'name': 'tea_bags', 'max_capacity': 50, 'quantity': 50, 'unit_of_measure': 'init'},
        {'name': 'milk', 'max_capacity': 250, 'quantity': 250, 'unit_of_measure': 'ml'}
    ]

    # Fill ingredients in the database
    for ingredient_data in initial_ingredients:
        db_ingredient = Ingredient(**ingredient_data)
        session.add(db_ingredient)
    session.commit()
    

def refill_all_ingredients(session):
    ingredient_manager = IngredientManager(session)
    ingredients = [
        {'name': 'water', 'quantity_to_add': 500},
        {'name': 'coffee_beans', 'quantity_to_add': 180},
        {'name': 'tea_bags','quantity_to_add': 20},
        {'name': 'milk', 'quantity_to_add': 200}
    ]
    
    for ingredient in ingredients:
        ingredient_manager.refill_ingredient(ingredient.name, ingredient.quantity_to_add)