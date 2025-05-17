class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        
        self.all_coffees.append(self)
        self._orders = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Coffee name should be a string')
        if len(value) < 3:
            raise ValueError('Coffee name should be not less than 3 characters')
        self._name = value

    def orders(self):
        return self._orders
    
    def customers(self):
        return list({order.customer for order in self._orders}) # unique list of customers for this coffee type
    
    def num_orders(self):
        return len(self._orders) # total no of times of orders for this coffee
    
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        count = len(self._orders)
        return total / count # average price for this coffee based on its orders