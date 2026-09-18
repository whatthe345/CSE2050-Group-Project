from product import Product 

class ShoppingCart:
    def __init__(self):
        """Intializes a new empty shoppingcart"""
        self.items = []


    def add_product(self,product):
        """Adds a product object to the shopping items"""

        self.items.append(product)


    def remove_product(self, product_id: str):
        "Removes a product object from the shopping items if the product_id is available"

        for prod in self.items: 
            if prod.get_id() == product_id: 
                self.items.remove(prod)
                return True
        return False
    def get_items(self):
        "Returns all the product objects in the shoppingcart"

        return self.items

        
    def calculate_total(self):
        """Calculates and returns the total cost of all the products in the shopping items"""

        total = 0
        for item in self.items: 
            total += item.get_price()
        return total
    def is_empty(self):
        """Returns True if the car has no items, False otherwise"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def __repr__(self):
        """Returns string summary of th items items"""
        return f'ShoppingCart({self.items})'




    