import unittest
from unittest.mock import Mock, patch
from beverage_machine import CoffeeMachine

# Integration tests verify that different components of the application work together as expected.

class TestCoffeeMachineIntegration(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.mock_ingredient_manager = Mock()
        self.coffee_machine = CoffeeMachine(self.mock_session, self.mock_ingredient_manager)

    @patch('builtins.input', side_effect=["yes", "yes", "2"])
    def test_make_coffee_integration(self, mock_input):
        result = self.coffee_machine.make_coffee()
        self.assertIn("Enjoy your coffee!", result)
        self.mock_session.commit.assert_called()

    @patch('builtins.input', side_effect=["1"])
    def test_make_tea_integration(self, mock_input):
        result = self.coffee_machine.make_tea()
        self.assertIn("Enjoy your tea!", result)
        self.mock_session.commit.assert_called()

if __name__ == "__main__":
    unittest.main()
