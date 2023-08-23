
from src.beverage_machine import CoffeeMachine


def main():
    # Initialize the CoffeeMachine
    beverage_machine = CoffeeMachine()

    welcome = 'Welcome to the Hot Beverage Machine!\n'
    print(welcome)

    how_to_shut = 'Enter X to shutdown the machine!\n'
    print(how_to_shut)

    while True:
        # Gather user input for beverage customization
        beverage_choice = input(
            'Would you like 1 - Coffee or 2 - Tea? (1 or 2, or X): ').lower()
        if beverage_choice == '1':
            # Make a coffee beverage
            coffee_result = beverage_machine.make_coffee()
            print(coffee_result)
        elif beverage_choice == '2':
            # Make a tea beverage
            tea_result = beverage_machine.make_tea()
            print(tea_result)
        elif beverage_choice == 'r':
            # Re-fill all the igredients
            refill_result = beverage_machine.refill_all_ingredients()
            print(refill_result)
        elif beverage_choice == 'x':
            # Shut down the machine
            shutting_down = 'Shutting down the Hot Beverage Machine! ...\n'
            print(shutting_down)
            break
        else:
            invalid_beverage_choice = 'You\'ve entered an invalid beverage choice, enter 1 or 2.\n'
            print(invalid_beverage_choice)


if __name__ == '__main__':
    main()
