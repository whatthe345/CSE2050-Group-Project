from product import Product
from customer import Customer 
from order import Order
from order_queue import OrderQueue
from stack import Stack
class Store: 
    
    def __init__(self):
        """Initializes a store with empty product and customer records and order logs"""
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.processed = Stack()
        self.order_counter = 0

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
    def find_order(self, order_id: str):
        """Finds and returns an Order by ID, or None if not found"""
 
        for order in self.orders:
            if order.get_id() == order_id:
                return order
        return None
    def get_orders(self):
        return list(self.orders)
    def checkout(self, customer_id: str):
        """Creates an Order from the customer's cart, adds it to the
        store's orders, enqueues it, clears the cart, and returns it.
        Returns None for an unknown customer or empty cart."""
 
        customer = self.find_customer(customer_id)
        if customer is None:
            return None
 
        cart = customer.get_cart()
        if cart.is_empty():
            return None
 
        self.order_counter += 1
        order_id = f"O{self.order_counter}"
 
        # Copy the items so clearing the cart doesn't affect the order
        order = Order(order_id, customer, list(cart.get_items()))
 
        self.orders.append(order)
        self.order_queue.enqueue(order)
        cart.clear()
        return order
    def process_next_order(self):
        """Dequeues the oldest waiting order. Returns None if no order is waiting."""
 
        order = self.order_queue.dequeue()
        if order is None:
            return None
 
        order.set_status("PROCESSING")
        self.processed.push(order)
        return order
    def get_order_history(self):
        """Returns a list of all processed orders"""
 
        history = []
        while not self.processed.is_empty():
            history.append(self.processed.pop())
 
        # Push back oldest-first so the original stack order is restored
        for order in reversed(history):
            self.processed.push(order)
 
        return history

