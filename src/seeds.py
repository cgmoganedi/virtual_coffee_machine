
from models import Ingredient

def seed_ingredients(session)-> None:
    # Ingredient names and their initial quantities
    initial_ingredients = [
        {'name': 'water', 'max_capacity': 750, 'unit_of_measure': 'ml'},
        {'name': 'coffee_beans', 'max_capacity': 250, 'unit_of_measure': 'grams'},
        {'name': 'tea_bags', 'max_capacity': 50, 'unit_of_measure': 'unit'},
        {'name': 'milk', 'max_capacity': 250, 'unit_of_measure': 'ml'}
    ]

    try:
        # Fill ingredients in the database
        for ingredient_data in initial_ingredients:
            db_ingredient = Ingredient(**ingredient_data)
            session.add(db_ingredient)
        session.commit()
    except ValueError as e:
        print('Could not seed.', e)
    

def refill_all_ingredients(ingredient_manager)-> str:
    ingredients = [
        {'name': 'water'},
        {'name': 'coffee_beans'},
        {'name': 'tea_bags'},
        {'name': 'milk'}
    ]
    
    try:
        for ingredient in ingredients:
            ingredient_manager.refill_ingredient(ingredient['name'])
            
        return 'Successfully refilled all the ingredients'
    
    except ValueError as e:
        print('Could not re-fill.', e)