class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        self.all_orders.extend([self])
        
        customer._orders.extend([self]) # add to customer order list
        coffee._orders.extend([self]) # add to coffee order list
    
    def __repr__(self):
        return f"Order(customer='{self.customer.name}', coffee='{self.coffee.name}', price={self.price})" # string representation of the order
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError('The customer does not exist')
        self._customer = value
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee 
        if not isinstance(value, Coffee):
            raise TypeError('The coffee does not exist')
        self._coffee = value
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price should be a number (1.0 - 10.0)')
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError('Price should be between 1.0 and 10.0')
        self._price = float(value)
