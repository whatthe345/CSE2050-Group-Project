from product import Product 

class ShoppingCart:
    def __init__(self):
        """Intializes a new empty shoppingcart"""
        self.cart = []


    def add_product(self,product):
        """Adds a product object to the shopping cart"""

        self.cart.append(product)


    def remove_product(self, product_id: str):
        "Removes a product object from the shopping cart if the product_id is available"

        for prod in self.cart: 
            if prod.get_id() == product_id: 
                self.cart.remove(prod)
                return True
        return False
    def get_items(self):
        "Returns all the product objects in the shoppingcart"

        return self.cart

        
    def calculate_total(self):
        """Calculates and returns the total cost of all the products in the shopping cart"""

        total = 0
        for item in self.cart: 
            total += item.get_price()
        return total
    def is_empty(self):
        """Returns True if the car has no items, False otherwise"""
        if len(self.cart) == 0:
            return True
        else:
            return False

    def __repr__(self):
        """Returns string summary of th cart items"""
        return f'ShoppingCart({self.cart})'




    