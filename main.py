import csv

class Item:
    pay_rate= 0.8 # The pay rate after 20% discount 
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the recieved arguments
        assert price >= 0, f"Price {price} should be greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to 0"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} should be greater than or equal to 0"

        self.broken_phones = broken_phones

item1 = Item("Samsung s22", 200)
phone1 = Phone("iPhone 12", 1000, 5,1)
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)