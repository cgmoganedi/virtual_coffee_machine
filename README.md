# virtual_coffee_machine


# Coffee Machine Simulation


## Introduction

The Coffee Machine Simulation is designed to replicate the experience of using a coffee machine to brew beverages. It provides an interactive interface for users to make coffee and tea with customizable options. The simulation tracks ingredient levels,  warns if any ingredient is too low, handles refills, and records each served beverage.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Assumptions](#assumptions)
- [Future Features](#future-features)
- [Coffee and Tea Making Process](#coffee-and-tea-making-process)
- [Implementation Overview](#implementation-overview)
- [Testing (Optional)](#testing-optional)

## Features
Create customized coffee and tea beverages.
Manage ingredient levels (water, milk, coffee beans) and receive warnings for low levels.
Allows ingredient re-fills.
Record served beverages.

## How to Use

1. Clone the repository to your local machine.
2. Create and activate virtual enviroment.
3. Install the required packages.
4. Set up the database and tables for ingredient management and served beverages.
5. Run the `src/main.py` script to interact with the Coffee Machine Simulation.
6. Follow the on-screen prompts to select options and make coffee or tea.


## Installation

1. Clone the repository:
   `git clone https://github.com/cgmoganedi/virtual_coffee_machine.git && cd virtual_coffee_machine`

2. Set up a virtual environment:
    Make sure you have Python >= 3.11 installed on the system then create a virtual environment and activate it like so:
    `python -m venv venv && source venv/Scripts/activate` or `python -m venv venv && ./venv/Scripts/activate` depending on the terminal used.

3. Install the required packages:
    `pip install -r requirements.txt` or manually like so: `pip install python-dotenv pytest pytest-cov pytest-html`

4. Create a `.env` file in the project root and add your Dropbox access token :
    `cp .env.example .env`
    and add or modify in it to the correct env values:
    DATABASE_URL=<your_database_url_here>

## Assumptions

- Each beverage costs 200ml or 150 ml of water and 50 ml of milk (if added).
- A coffee beans (or tea bags) do not contribute to the volume of the beverage served.
- The maximum capacity for water, milk, and coffee beans, tea bags is 750 ml, 250 ml, 250 grams, and 50 units, respectively.
- The cup to pour into has a total rated capacity of 200 ml.
- Strength-1 coffee requires 5g of coffee beans, strength-2 requires 10g, and strength-3 requires 15g.
- Strength-1 tea requires 1 unit of a tea bag, strength-2 requires 2, and strength-3 requires 3.
- Whenever we re-fill an ingredient we fill it to max capacity.
- The application assumes a SQL database for data storage.

## Future Features
- Support for additional beverages, options and customizations (e.g., hot chocolate).
- Integration with a GUI for a more interactive user experience.
- User profiles for personalized preferences.
- Integration with a payment system for ordering and payment processing.
- Remote access and control of the coffee machine.

## Coffee and Tea Making Process
The coffee and tea making processes are implemented through the `Coffee` and `Tea` classes. These classes represent the base for their respective beverages and encapsulate the brewing logic based on user preferences.

- Coffee:
  - Options: Milk (yes/no), Froth (yes/no), Strength (1, 2, or 3)
  - Ingredients: Water, Coffee Beans, Milk (optional)
  - Process: Check ingredient levels -> Brew -> Update ingredient levels

- Tea:
  - Options: Strength (1, 2, or 3)
  - Ingredients: Water
  - Process: Check ingredient levels -> Brew -> Update ingredient levels

The chosen implementation approach ensures modularity and separation of concerns, making it easier to maintain and extend the simulation for future features. Furthermore, The tea and coffee making processes share a common base class, Beverage, which handles ingredient checks and updates. Specific beverage classes (Coffee and Tea) implement brewing logic based on user input.

Lastly, the relationship between tea and coffee classes allows for code reusability while accommodating unique brewing requirements for each beverage type.


## Implementation Overview
The Coffee Machine Simulation follows object-oriented programming (OOP) principles, design patterns, and best practices for clean and maintainable code. The program is structured with classes that represent different components of the coffee machine, ingredient management, and beverage making. These classes are designed to work together while adhering to single responsibility and open/closed principles.

This design supports team collaboration by providing clear boundaries and responsibilities for each class. Team members can work on different parts of the simulation independently and integrate their contributions seamlessly. The use of object-oriented design patterns such as inheritance, composition, and dependency injection enhances code modularity and testability.

For testing, the simulation include may (with enough time) unit tests, end-to-end tests, and integration tests to ensure the functionality, user interactions, and component interactions are thoroughly validated.

# Design Rationale
The chosen design follows object-oriented principles, including Single Responsibility, Open/Closed, and Dependency Inversion. This modular structure allows for easy maintenance and scalability. SQLAlchemy provides a robust data storage solution with version control for the application's state.

# Collaboration and Team Support
The design promotes collaboration by separating concerns into distinct classes. The use of SQLAlchemy and Alembic ensures consistent data storage and allows multiple team members to work simultaneously on different features.

To collaborate effectively:

    ◉ Team members can work on different modules (e.g., user input, ingredient management, beverage creation).
    ◉ Regular code reviews can ensure code quality and adherence to established patterns.
    ◉ Database migration scripts (Alembic) help manage changes to the data model, ensuring a consistent database state across the team.


## Testing (Optional)
Testing is a crucial aspect of software development to ensure that your code functions as intended, handles various scenarios, and maintains quality over time. We will cover unit testing, end-to-end testing, and integration testing for your virtual coffee machine simulation using the pytest framework. We'll also cover how to generate test reports and measure code coverage.

1. Unit Testing:

Unit tests focus on testing individual components (functions, methods, classes) in isolation. They help verify that each component behaves correctly.

Create a test_ingredients.py file for testing the IngredientManager class:

2. End-to-End Testing:

End-to-end tests simulate real user interactions, ensuring that the entire system functions correctly from start to finish.

Create a test_coffee_machine.py file for end-to-end testing:

3. Integration Testing:

Integration tests ensure that different components work together as expected.

Create a test_integration.py file for integration testing:


4. Test Reports and Coverage:

To run tests, generate reports, and measure coverage using pytest, follow these steps:

Install pytest and related packages if not already installed: `pip install pytest pytest-cov`
Run tests and generate reports: `pytest --cov=src --cov-report=html --junitxml junit.xml`

This command runs tests, measures coverage, and generates an HTML coverage report in the htmlcov directory.

Open the generated coverage report in a web browser:
Navigate to the htmlcov directory and open the index.html file in your web browser. This report shows the coverage details for each module and highlights lines that are covered or missed.

By following these steps, you can ensure that your virtual coffee machine simulation is thoroughly tested at various levels, and you can obtain comprehensive test reports and code coverage metrics to assess the quality of your code. Remember to adjust the filenames and content to match your project's structure and codebase.
