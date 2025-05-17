from order import Order
class Customer:
    all_customers = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        self.all_customers.append(self)
        self._orders = []
        
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
        new_order = Order(self, coffee, price)
        return new_order # places order for this customer
    
    