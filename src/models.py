import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, sessionmaker

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
        # Implement a method to represent the coffee cup as a string
        # Include information about milk, froth, strength, etc.
        return f"Your beverage cup served: ..."

class ServedBeverage(Base):
    """Records served beverages with timestamp, ingredients, and result."""
    __tablename__ = 'served_beverages'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    beverage_type = Column(Integer)
    milk_added = Column(Boolean)
    frothed_milk = Column(Boolean, nullable=True)
    strength = Column(Integer)
    result = Column(String)

    def __str__(self):
        # Implement a method to represent the coffee cup as a string
        # Include information about milk, froth, strength, etc.
        return f"Your beverage cup served: ... {self.result}"

class IngredientRefill(Base):
    """Tracks ingredient refills with timestamp and quantity added."""
    __tablename__ = 'ingredient_refills'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    quantity_added = Column(Integer)
    
    def __str__(self):
        # Implement a method to represent the coffee cup as a string
        # Include information about milk, froth, strength, etc.
        return f"Your refill: ..."
    

# Initialize the database engine and session
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
