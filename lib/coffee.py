class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self._name = name
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
