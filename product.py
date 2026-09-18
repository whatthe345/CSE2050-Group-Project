

class Product: 

    def __init__(self, product_id, name, price): 
        """Initializes a new proudct with an ID, name, and price"""
        self.product_id = product_id
        self.name = name 
        self.price = price


    def get_id(self): 
        """Returns the unique id of the product"""
        return self.product_id

    def get_name(self):
        """Returns the name of the product"""
        return self.name

    def get_price(self): 
        """Returns the price of the product as a floating point number"""
        return float(self.price)

    def __repr__(self):
        "Returns a string version of the Product"
        return f"Product({self.product_id}) , '{self.name}', ${self.price})"


