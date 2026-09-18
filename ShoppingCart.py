from Product import product

class ShoppingCart:
    def __init__(self):
        self.cart = list()
    def add_product(self,product):
        self.cart.append(product)
    def remove_product(self, product_id: product.get_id):
        
        if product_id in self.cart:
            self.cart.remove(product_id)
            return True
        else:
            return False
    def get_items(self):
      
        
        return self.cart
    def calculate_total(self):
        i=0
        total=0
        for i in len(self.cart):
            total = total + Product.get_price(self.cart(i))
            i=i+1
        
        return total
    def is_empty(self):
        if len(self.cart) == 0:
            return True
        else:
            return False
    
