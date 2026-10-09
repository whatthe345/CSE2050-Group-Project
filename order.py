from customer import Customer
from product import Product
def make_list(n):
    if hasattr(n, '__iter__'):
        return n
    else:
        return [n]
class Order:
    """Stores a snapshot of the customer’s purchased products."""

    def __init__(self, order_id: str, customer: Customer, items: list[Product]):
        """Create an order."""
        status = "PENDING"
        self.stat= status
        self.order_id = order_id
        self.customer = customer
        self.items = items
    def get_id(self):
        return self.order_id
    def get_customer(self):
        return self.customer
    def get_items(self):
        return self.items
    def get_status(self):
        return self.stat
    def set_status(self,status: str) :
        if status == "PENDING" or status == "PROCESSING" or status == "COMPLETED":
            self.stat = status
            print("Status Set")
        else:
            print("Invalid Status")
    def calculate_total(self):
        i=0
        total = 0
        for i in make_list(len(self.items)):
            total = total + self.items[i].get_price()
            i = i + 1
