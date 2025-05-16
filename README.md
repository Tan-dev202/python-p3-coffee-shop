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
2. Set up a virtual environment:
    > **pipenv install**
    > **pipenv shell**
3. Install pytest for testing:
    > **pipenv install pytest**

## Testing
+ Run tests using pytest: **pytest**

+ You can also run debug.py to see a demonstration of the functionality: **python lib/debug.py**

# Author
Enock Tangus