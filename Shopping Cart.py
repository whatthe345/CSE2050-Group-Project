import Product
class ShoppingCart:
    def __init__(self):
        self.cart = list()
    def add_product(self,product: Product):
        self.cart.append()
    def remove_product(self, product_id: Product.product_id):
        
        if product_id in self.cart:
            self.cart.remove(product_id)
            return True
        else:
            return False
    def get_items():
    