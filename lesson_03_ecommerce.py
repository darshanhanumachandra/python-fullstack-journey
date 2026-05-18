class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_final_price(self):
        """Override this in child classes"""
        pass

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
        self.shipping_cost = weight * 10  # $10 per kg
    
    def get_final_price(self):
        """Physical products have shipping"""
        final_price = self.price + self.shipping_cost
        return final_price


class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_final_price(self):
        """Digital products have no shipping"""
        return self.price

"""
physical = PhysicalProduct("Laptop", 1000, 2)
digital = DigitalProduct("Python Course", 50)

print(f"{physical.name}: ${physical.get_final_price()}")
print(f"{digital.name}: ${digital.get_final_price()}")
"""

# Creating multiple products
products = [
    PhysicalProduct("Laptop", 1000, 2),
    DigitalProduct("Python Course", 50),
    PhysicalProduct("Book", 30, 0.5),
    DigitalProduct("Ebook", 15)
]

# Loop through all and print prices
for product in products:
    print(f"{product.name}: ${product.get_final_price()}")
