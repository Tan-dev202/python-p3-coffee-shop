class Customer:
    all_customers = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        Customer.all_customers.append(self)
        self._orders = []
    
    def __repr__(self):
        return f"Customer(name='{self.name}')" # string representation of the customer
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name should be a string')
        if not (1 <= len(value) <= 15):
            raise ValueError('Name should be 1 to 15 characters in length')
        self._name = value

    def orders(self):
        return self._orders # all orders for this customer
    
    def coffees(self):
        return list({order.coffee for order in self._orders}) # unique list of coffees for this customer
    
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order # places order for this customer
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None # when there are no customers for the specified coffee
        
        spending = {}
        
        for order in coffee.orders():
            spending[order.customer] = spending.get(order.customer, 0) + order.price
        
        return max(spending, key=spending.get, default=None) # customer who spent the most on the specified coffee
