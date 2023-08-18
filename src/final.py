from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Ingredient(Base):
    """Represents ingredients and their quantities in the machine."""
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)  # Ingredient name (e.g., water, milk)
    quantity = Column(Float)  # Current quantity available
    max_capacity = Column(Float)  # Maximum capacity

class ServedBeverage(Base):
    """Records served beverages with timestamp, ingredients, and result."""
    __tablename__ = 'served_beverages'

    id = Column(Integer, primary_key=True)
    beverage_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ingredients = Column(String)
    result = Column(String)

class IngredientRefill(Base):
    """Tracks ingredient refills with timestamp and quantity added."""
    __tablename__ = 'ingredient_refills'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    quantity_added = Column(Float)

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
        else:
            raise ValueError(f"Ingredient {ingredient_name} not found")

class Beverage:
    """Base class for beverages like coffee and tea."""
    def __init__(self, session, ingredient_manager):
        self.session = session
        self.ingredient_manager = ingredient_manager

    def check_ingredient_levels(self, required_ingredients):
        """Check if there are enough ingredients to make the beverage."""
        for ingredient_name, required_quantity in required_ingredients.items():
            ingredient = self.ingredient_manager.get_ingredient(ingredient_name)
            if not ingredient or ingredient.quantity < required_quantity:
                raise ValueError(f"Not enough {ingredient_name} to make the beverage")

    def update_ingredient_levels(self, used_ingredients):
        """Update ingredient levels after serving the beverage."""
        for ingredient_name, used_quantity in used_ingredients.items():
            ingredient = self.ingredient_manager.get_ingredient(ingredient_name)
            ingredient.quantity -= used_quantity
            self.session.commit()

class Coffee(Beverage):
    """Represents a coffee beverage."""
    def __init__(self, session, ingredient_manager, milk, froth, strength):
        super().__init__(session, ingredient_manager)
        self.milk = milk
        self.froth = froth
        self.strength = strength

    def brew(self):
        """Brew a coffee based on milk, froth, and strength options."""
        required_ingredients = {
            'water': 150,
            'coffee_beans': 5 * self.strength,
        }
        if self.milk:
            required_ingredients['milk'] = 50
        self.check_ingredient_levels(required_ingredients)

        used_ingredients = {'water': 150}
        if self.milk:
            used_ingredients['milk'] = 50
        self.update_ingredient_levels(used_ingredients)

        self.session.add(ServedBeverage(beverage_type='coffee', ingredients=str(required_ingredients), result="success"))
        self.session.commit()

        return "Enjoy your coffee!"

class Tea(Beverage):
    """Represents a tea beverage."""
    def __init__(self, session, ingredient_manager, strength):
        super().__init__(session, ingredient_manager)
        self.strength = strength

    def brew(self):
        """Brew a tea based on strength option."""
        required_ingredients = {
            'water': 150,
        }
        self.check_ingredient_levels(required_ingredients)

        used_ingredients = {'water': 150}
        self.update_ingredient_levels(used_ingredients)

        self.session.add(ServedBeverage(beverage_type='tea', ingredients=str(required_ingredients), result="success"))
        self.session.commit()

        return "Enjoy your tea!"

class CoffeeMachine:
    """Simulates a coffee machine and handles beverage making."""
    def __init__(self, session, ingredient_manager):
        self.session = session
        self.ingredient_manager = ingredient_manager

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

def main():
    # Set up SQLAlchemy engine and create database tables here

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Initialize IngredientManager
    ingredient_manager = IngredientManager(session)

    # Initialize CoffeeMachine
    coffee_machine = CoffeeMachine(session, ingredient_manager)

    # Make a coffee with milk, froth, and strength 2
    coffee_result = coffee_machine.make_coffee(milk=True, froth=True, strength=2)
    print(coffee_result)

    # Make a tea with strength 1
    tea_result = coffee_machine.make_tea(strength=1)
    print(tea_result)

if __name__ == "__main__":
    main()
