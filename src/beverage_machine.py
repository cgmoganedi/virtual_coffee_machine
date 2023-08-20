from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from beverage import Coffee, Tea
from models import Base, Ingredient, IngredientRefill

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


database_url = 'LIDIHOGIHODGIH'

class IngredientManager:
    """Manages ingredient levels and refills."""
    def __init__(self, session):
        self.session = session

    def get_ingredient(self, ingredient_name):
        """Retrieve an ingredient by its name."""
        return self.session.query(Ingredient).filter_by(name=ingredient_name).first()

    def refill_ingredient(self, ingredient_name, quantity_added):
        """Refill an ingredient by updating its quantity."""
        ingredient = self.get_ingredient(ingredient_name)
        if ingredient:
            new_quantity = ingredient.quantity + quantity_added
            if new_quantity > ingredient.max_capacity:
                raise ValueError(f"Refilling exceeds max capacity for {ingredient_name}")
            ingredient.quantity = new_quantity
            self.session.add(IngredientRefill(ingredient_id=ingredient.id, quantity_added=quantity_added))
            self.session.commit()
            print('Success fully increased {ingredient_name} by {quantity_added}')
        else:
            raise ValueError(f"Ingredient {ingredient_name} not found")

class CoffeeMachine:
    """Simulates a coffee machine and handles beverage making."""
    def __init__(self):
        # Set up SQLAlchemy engine, database tables and create a session
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        # Initialize IngredientManager
        self.ingredient_manager = IngredientManager(self.session)


    def gather_user_input(self):
        """Gather user input for milk, froth, and strength."""
        milk = input("Add milk? (yes/no): ").lower() == "yes"
        froth = False
        if milk:
            froth = input("Froth milk? (yes/no): ").lower() == "yes"
        strength = int(input("Select strength (1, 2, or 3): "))
        return milk, froth, strength
    
    def make_coffee(self, milk, froth, strength):
        """Make a coffee with specified options."""
        milk, froth, strength = self.gather_user_input()
        coffee = Coffee(self.session, self.ingredient_manager, milk, froth, strength)
        try:
            result = coffee.brew()
            return result
        except ValueError as e:
            return str(e)

    def make_tea(self, strength):
        """Make a tea with specified strength."""
        strength = int(input("Select strength for tea (1, 2, or 3): "))
        tea = Tea(self.session, self.ingredient_manager, strength)
        try:
            result = tea.brew()
            return result
        except ValueError as e:
            return str(e)
        
