from product import Product
from customer import Customer 

class Store: 
    
    def __init__(self):
        """Initializes a store with empty product and customer records"""
        self.products = []
        self.customers = []

    def add_product(self, product: Product):
        """Adds a product to product inventroy if product id doesn't exist"""

        for prod in self.products:
            if prod.get_id() == product.get_id():
                return False 

        self.products.append(product)
        return True

    def find_product(self, product_id: str):

        for prod in self.products: 
            if prod.get_id() == product_id:
                return prod
        return None


    def add_customer(self, customer:Customer):
        """Registers a customer if their customer ID is unique"""
        
        for cust in self.customers: 
            if cust.get_id() == customer.get_id():
                return False 

        self.customers.append(customer)
        return True

    def find_customer(self, customer_id: str):
        """Searches for and returns a customer by ID, or None if not found""" 

        for cust in self.customers: 
            if cust.get_id() == customer_id: 
                return cust

        return None

