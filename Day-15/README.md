# Coffee Machine Program

Welcome to the Coffee Machine Program! This program simulates a coffee machine that allows you to choose from various coffee options and make your favorite drink. Let's get brewing!

## Overview

The Coffee Machine Program provides the following features:

- Selection of coffee options: espresso, latte, cappuccino
- Resource management: checks if the required ingredients are sufficient
- Coin processing: accepts coins and calculates the total payment
- Transaction handling: determines if the payment is successful and provides change if applicable
- Coffee making: prepares the selected drink by deducting the required resources
- Reporting: displays the current status of available resources and profit

## Dependencies

This program has the following dependencies:

- `menu.py`: A module containing the menu options and drink recipes.
- `resources.py`: A module containing the available resources for making coffee.

## Getting Started

To start the Coffee Machine Program, run the Python script `coffee_machine.py`. The program will prompt you to enter your coffee choice (espresso/latte/cappuccino) and guide you through the payment and coffee-making process. You can also use the command 'off' to turn off the coffee machine or 'report' to view the current status of resources and profit.

## Customization

You can customize the available coffee options and their recipes by modifying the `MENU` dictionary in the `menu.py` module. Each drink option consists of its name, ingredients, and cost.

You can also adjust the initial resources by modifying the `resources` dictionary in the `resources.py` module. The available resources include water, milk, and coffee.

Feel free to experiment with different drink options and resource quantities to create your perfect coffee machine experience!

## Enjoy Your Coffee!

Sit back, relax, and enjoy your freshly brewed cup of coffee from the Coffee Machine Program. Whether you prefer an espresso, latte, or cappuccino, this program has got you covered. Start brewing now and satisfy your coffee cravings!

Cheers!
