from Product import Product
from ShoppingCart import ShoppingCart

class customer: 
    def __init__(self,customer_id: str, customer_name: str):
        self.customer_id = customer_id
    
        self.name=customer_name
        self.cart=ShoppingCart()
   
    def get_id(self):
        return self.customer_id
    def get_name(self):
        return self.name
    def get_shoppingcart(self):
        return self.cart
    
    

    
    