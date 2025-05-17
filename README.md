# Coffee Shop

This project implements a domain model for a Coffee Shop utilizing Object-Oriented Principles in Python programming.

## Overview
The model has the following entities:
- [x] Customer: Individuals who purchase coffee
- [x] Coffee: Types of coffee available
- [x] Order: Links customers with their coffee orders

The relationships are:

**Many-to-Many (through Order entity):**
+ Many customers can purchase many types of coffee

**One-to-Many:**
+ A customer can place many orders
    - Each order is assigned to only one customer
+ A coffee type can be included in many orders
    - Each order has one coffee type (quantity may vary)

## Setup Instructions
1. Clone this repository.
2. On the terminal, set up a virtual environment:

    pipenv install
    pipenv shell

## Testing and Debugging
1. Run the debug.py file from the terminal:
    
    python debug.py

2. Examples (can be modified) in the file will be executed and the output will be shown.

# Author
Enock Tangus