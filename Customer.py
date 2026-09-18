from product import Product
from cart import ShoppingCart

class Customer: 
    def __init__(self,customer_id: str, customer_name: str):
        """Intializes a new customer with a unique ID, a name , and cart"""
        self.customer_id = customer_id
    
        self.name=customer_name
        self.cart=ShoppingCart()
   
    def get_id(self):
        """Returns unique ID of customer"""
        return self.customer_id
    def get_name(self):
        """Returns name of customer"""
        return self.name
    def get_cart(self):
        """Returns the customer's shoppingcart instance"""
        return self.cart
    
    

    