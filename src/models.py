import os
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
Base = declarative_base()

class Ingredient(Base):
    """Represents ingredients and their quantities in the machine."""
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)  # Ingredient name (e.g., water, milk)
    quantity = Column(Integer, default=0)  # Current quantity available
    max_capacity = Column(Integer)  # Maximum capacity
    unit_of_measure = Column(String)  # e.g., ml, grams
    
    def __str__(self):
        # Represent the beverage ingredient as a string
        return f"Your beverage ingredient: ...{self.name}"

class ServedBeverage(Base):
    """Records served beverages with timestamp, ingredients, and result."""
    __tablename__ = 'served_beverages'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    beverage_type = Column(String)
    milk_added = Column(Boolean, default=False)
    strength = Column(Integer)
    frothed_milk = Column(Boolean, nullable=True)
    result = Column(String)

    def __str__(self):
        # Represent the coffee cup as a string
        # Includes information about milk, froth, strength, etc.
        return f"Your beverage cup served: ... <ServedBeverage(type='{self.beverage_type}', timestamp='{self.timestamp}', result='{self.result}')>"

class IngredientRefill(Base):
    """Tracks ingredient refills with timestamp and quantity added."""
    __tablename__ = 'ingredient_refills'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    quantity_added = Column(Integer)
    
    def __str__(self):
        # Represent the coffee cup as a string
        # May include information about milk, froth, strength, etc.
        return f"Your refill: ...{self.ingredient_id} added {self.quantity_added}"
    
# Initialize the database engine and create tables if they don't exist
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
