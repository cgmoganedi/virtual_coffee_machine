import unittest
from unittest.mock import patch
from beverage_machine import CoffeeMachine

# End-to-end tests cover the entire workflow of the application, simulating user interactions and verifying the final outcome.
class TestCoffeeMachineEndToEnd(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.mock_ingredient_manager = Mock()
        self.coffee_machine = CoffeeMachine(self.mock_session, self.mock_ingredient_manager)

    @patch('builtins.input', side_effect=["yes", "yes", "2"])
    def test_make_coffee_with_user_input(self, mock_input):
        result = self.coffee_machine.make_coffee()
        self.assertIn("Enjoy your coffee!", result)

    @patch('builtins.input', side_effect=["1"])
    def test_make_tea_with_user_input(self, mock_input):
        result = self.coffee_machine.make_tea()
        self.assertIn("Enjoy your tea!", result)

if __name__ == "__main__":
    unittest.main()
