# Coffee Shop

This project implements a domain model for a Coffee Shop utilizing Object-Oriented Principles in Python programming.

## Overview
The model has the following entities:
- [x] `Customer`: Individuals who purchase coffee
- [x] `Coffee`: Types of coffee available
- [x] `Order`: Links customers with their coffee orders

The relationships are:

**Many-to-Many (through Order entity):**
+ Many `customers` can purchase many types of `coffee`

**One-to-Many:**
+ A `customer` can place many `orders`
    - Each `order` is assigned to one `customer`
+ A `coffee` type can be included in many `orders`
    - Each `order` belongs to one `coffee`

## Structure

    coffee_shop/
        |── customer.py
        |── coffee.py
        |── order.py
        └── debug.py


## Setup Instructions
1. Clone this repository.
2. On the terminal, set up a virtual environment:

    `pipenv install`
    
    `pipenv shell`

## Classes
### Customer
The `Customer` class represents an individual who orders coffee.

Properties:

+ `name`: A string between 1 and 15 characters.

Methods:

+ `orders()`: Returns a list of all orders for this customer
+ `coffees()`: Returns a unique list of coffees that the customer has ordered
+ `create_order(coffee, price)`: Places a new order with this customer and the given coffee and price
+ `most_aficionado(coffee) (class method)`: Returns the customer who has spent the most money on the specified coffee

### Coffee
The Coffee class represents a type of coffee that can be ordered.

Properties:

+ `name`: String at least 3 characters long

Methods:

+ `orders()`: Returns a list of all orders for this coffee
+ `customers()`: Returns a unique list of customers who have ordered this coffee
+ `num_orders()`: Returns the total number of times this coffee has been ordered
+ `average_price()`: Returns the average price for this coffee based on its orders

### Order
The `Order` class represents an association between a customer and a coffee.

Properties:

+ `customer`: A Customer instance
+ `coffee`: A Coffee instance
+ `price`: Float between 1.0 and 10.0

## Testing and Debugging
1. Run the debug.py file from the terminal:
    
    `python debug.py`

2. Examples (which can be modified) in the `debug.py` file will be executed and the output will be shown.

# Author
Enock Tangus