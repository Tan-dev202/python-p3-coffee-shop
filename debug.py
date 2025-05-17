from customer import Customer
from coffee import Coffee
from order import Order

def main():

    print("Adding customers...")
    anne = Customer("Anne")
    david = Customer("David")
    james = Customer("James")
    print(f"Customers added: {[customer.name for customer in Customer.customers]}")

    print("\nAdding coffees...")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    latte = Coffee("Latte")
    print(f"Coffees added: {[coffee.name for coffee in Coffee.coffees]}")

    print("\nPlacing orders...")
    anne.create_order(espresso, 3.75)
    anne.create_order(espresso, 3.50)
    anne.create_order(cappuccino, 4.25)
    
    david.create_order(espresso, 3.75)
    david.create_order(cappuccino, 4.25)
    david.create_order(latte, 4.75)
    david.create_order(latte, 4.50)
 
    james.create_order(latte, 4.75)
    james.create_order(latte, 4.50)
    james.create_order(latte, 4.25)
    
    print(f"Total orders placed: {len(Order.orders)}")

    print("\nTesting customer methods...")
    print(f"Anne's orders: {len(anne.orders())}")
    print(f"Anne's coffees: {[coffee.name for coffee in anne.coffees()]}")
    
    print("\nTesting coffee methods...")
    print(f"Espresso orders: {espresso.num_orders()}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
    print(f"Espresso average price: {espresso.average_price():.2f}")
    
    print(f"latte orders: {latte.num_orders()}")
    print(f"latte customers: {[customer.name for customer in latte.customers()]}")
    print(f"latte average price: {latte.average_price():.2f}")
    
    print("\nTesting most_aficionado method...")
    top_espresso_buyer = Customer.most_aficionado(espresso)
    print(f"Top espresso customer: {top_espresso_buyer.name if top_espresso_buyer else 'None'}")
    
    top_latte_buyer = Customer.most_aficionado(latte)
    print(f"Top latte customer: {top_latte_buyer.name if top_latte_buyer else 'None'}")
    
    print("\nAdding a new customer...")
    frank = Customer("frank")
    frank.create_order(cappuccino, 4.25)
    frank.create_order(latte, 4.75)
    print(f"Frank's orders: {len(frank.orders())}")
    print(f"Frank's coffees: {[coffee.name for coffee in frank.coffees()]}")

    print("\nAverage prices of all the coffees:")
    for coffee in Coffee.coffees:
        print(f"{coffee.name}: {coffee.average_price():.2f}")

if __name__ == "__main__":
    main()
    