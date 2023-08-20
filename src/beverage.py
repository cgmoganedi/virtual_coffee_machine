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