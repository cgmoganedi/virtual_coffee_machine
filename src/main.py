
from beverage_machine import CoffeeMachine

def main():
    # Initialize the CoffeeMachine
    beverage_machine = CoffeeMachine()
    
    welcome = 'Welcome to the Hot Beverage Machine!\n'
    print(welcome)
    
    how_to_shut = 'Enter X to shutdown the machine!\n'
    print(how_to_shut)
    
    while True:
        # Gather user input for beverage customization
        beverage_choice = input('Would you like 1 - Coffee or 2 - Tea? (1 or 2, or X): ')
        if int(beverage_choice) == 1:
            # Make a coffee beverage
            coffee_result = beverage_machine.make_coffee()
            print(coffee_result)
        elif int(beverage_choice) == 2:
            # Make a tea beverage
            tea_result = beverage_machine.make_tea()
            print(tea_result)
        elif beverage_choice.lower() == 'x':
            # Shut down the machine
            shutting_down = 'Shutting down the Hot Beverage Machine! ...\n'
            print(shutting_down)
            break
        else:
            beverage_doesnt_exist = 'Beverage does not exist!\n'
            print(beverage_doesnt_exist)

if __name__ == '__main__':
    main()
