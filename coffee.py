class Coffee:
    coffees = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        
        Coffee.coffees.append(self)
        self._orders = []
    
    def __repr__(self):
        return f"Coffee(name='{self.name}')"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Coffee name should be a string')
        if len(value) < 3:
            raise ValueError('Coffee name should be at least 3 characters long')
        self._name = value

    def orders(self):
        return self._orders
    
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
