

class Product: 

    def __init__(self, product_id, name, price): 
        self.product_id = product_id
        self.name = name 
        self.price = price


    def get_id(self): 
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self): 
        return float(self.price)

    def __repr__(self):
        return f"Product({self.product_id}) , '{self.name}', ${self.price})"


