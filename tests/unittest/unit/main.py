import unittest
from unittest.mock import Mock
from coffee_machine import IngredientManager, Coffee, Tea


# Unit tests focus on testing individual components or functions in isolation to ensure they behave as expected.

class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.mock_ingredient_manager = Mock(spec=IngredientManager)

    def test_coffee_brew_successful(self):
        self.mock_ingredient_manager.get_ingredient.return_value.quantity = 200
        coffee = Coffee(self.mock_session, self.mock_ingredient_manager, True, True, 2)
        result = coffee.brew()
        self.assertEqual(result, "Enjoy your coffee!")
        self.mock_session.commit.assert_called()

    def test_tea_brew_successful(self):
        self.mock_ingredient_manager.get_ingredient.return_value.quantity = 200
        tea = Tea(self.mock_session, self.mock_ingredient_manager, 1)
        result = tea.brew()
        self.assertEqual(result, "Enjoy your tea!")
        self.mock_session.commit.assert_called()

if __name__ == "__main__":
    unittest.main()
