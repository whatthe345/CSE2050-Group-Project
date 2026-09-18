from Product import product

class ShoppingCart:
    def __init__(self):
        self.cart = []
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
            total = total + product.get_price(self.cart(i))
            i=i+1
        
        return total
    def is_empty(self):
        if len(self.cart) == 0:
            return True
        else:
            return False


s1 = ShoppingCart()
p1 = product(1, 'Car',100)
p2 = product(2,'Ball',250)
s1.add_product(p1)
print(s1.get_items())
s1.add_product(p2)
print(s1.get_items())
    