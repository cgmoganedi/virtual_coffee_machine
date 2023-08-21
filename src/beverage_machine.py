import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from beverage import Coffee, Tea
from models import Base, Ingredient
from dotenv import load_dotenv

from seeds import refill_all_ingredients, seed_ingredients
# Load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


class IngredientManager:
    """Manages ingredient levels and refills."""
    def __init__(self, session):
        self.session = session

    def get_ingredient(self, ingredient_name):
        """Retrieve an ingredient by its name."""
        return self.session.query(Ingredient).filter_by(name=ingredient_name).first()

    def refill_ingredient(self, ingredient_name):
        """Refill an ingredient by updating its quantity."""
        ingredient = self.get_ingredient(ingredient_name)
        if ingredient:
            ingredient.quantity = ingredient.max_capacity
            self.session.commit()
            print(f'Successfully increased {ingredient_name} by {ingredient.max_capacity}')
        else:
            raise ValueError(f"Ingredient {ingredient_name} not found")

class CoffeeMachine:
    """Simulates a coffee machine and handles beverage making."""
    def __init__(self):
        # Set up SQLAlchemy engine, database tables and create a session
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        # Initialize IngredientManager
        self.ingredient_manager = IngredientManager(self.session)
        # Seed the ingredient at first
        # seed_ingredients(self.session)

    def refill_all_ingredients(self)-> str:
        return refill_all_ingredients(self.ingredient_manager)

    def gather_user_input(self):
        """Gather user input for milk, froth, and strength."""
        milk = input("Add milk? (yes/no): ").lower() == "yes"
        froth = False
        if milk:
            froth = input("Froth milk? (yes/no): ").lower() == "yes"
        strength = int(input("Select strength (1, 2, or 3): "))
        return milk, froth, strength
    
    def make_coffee(self):
        """Make a coffee with specified options."""
        milk, froth, strength = self.gather_user_input()
        coffee = Coffee(self.session, self.ingredient_manager, milk, froth, strength)
        try:
            result = coffee.brew()
            return result
        except ValueError as e:
            return str(e)

    def make_tea(self):
        """Make a tea with specified strength."""
        strength = int(input("Select strength for tea (1, 2, or 3): "))
        tea = Tea(self.session, self.ingredient_manager, strength)
        try:
            result = tea.brew()
            return result
        except ValueError as e:
            return str(e)
        
