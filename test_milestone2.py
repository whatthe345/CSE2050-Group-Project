import unittest
import contextlib
import io
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from product import Product
from customer import Customer
from order import Order
from store import Store

class TestLinkedList(unittest.TestCase):
    """Test the public behavior of LinkedList."""

    def test_empty_list(self):
        """Check the behavior of a new empty list."""
        items = LinkedList()

        self.assertTrue(items.is_empty())
        self.assertEqual(items.size(), 0)
        self.assertIsNone(items.get_first())
        self.assertIsNone(items.remove_first())

    def test_add_first(self):
        """Check that items are added to the beginning."""
        items = LinkedList()
        items.add_first("A")
        items.add_first("B")

        self.assertEqual(items.get_first(), "B")
        self.assertEqual(items.size(), 2)
        self.assertFalse(items.is_empty())
        self.assertEqual(items.remove_first(), "B")
        self.assertEqual(items.remove_first(), "A")

    def test_add_last(self):
        """Check that items are added to the end."""
        items = LinkedList()
        items.add_last("A")
        items.add_last("B")

        self.assertEqual(items.get_first(), "A")
        self.assertEqual(items.size(), 2)
        self.assertEqual(items.remove_first(), "A")
        self.assertEqual(items.remove_first(), "B")

    def test_remove_and_reuse(self):
        """Check mixed additions and reuse after becoming empty."""
        items = LinkedList()
        items.add_first("B")
        items.add_first("A")
        items.add_last("C")

        self.assertEqual(items.remove_first(), "A")
        self.assertEqual(items.size(), 2)
        self.assertEqual(items.get_first(), "B")
        self.assertEqual(items.remove_first(), "B")
        self.assertEqual(items.remove_first(), "C")
        self.assertTrue(items.is_empty())
        self.assertEqual(items.size(), 0)

        items.add_last("D")
        items.add_first("E")

        self.assertEqual(items.remove_first(), "E")
        self.assertEqual(items.remove_first(), "D")
        self.assertTrue(items.is_empty())


class TestStack(unittest.TestCase):
    """Test the public behavior of Stack."""

    def test_lifo(self):
        """Check that the last item added is removed first."""
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("C")

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), "C")
        self.assertEqual(stack.pop(), "B")
        self.assertEqual(stack.pop(), "A")
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

    def test_peek(self):
        """Check that peek returns the top item without removing it."""
        stack = Stack()
        stack.push("A")
        stack.push("B")

        self.assertEqual(stack.peek(), "B")
        self.assertEqual(stack.peek(), "B")
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), "B")

    def test_empty_and_reuse(self):
        """Check empty operations and reuse after removing all items."""
        stack = Stack()

        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())

        stack.push("A")
        self.assertEqual(stack.pop(), "A")
        self.assertIsNone(stack.pop())

        stack.push("B")
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), "B")


class TestOrderQueue(unittest.TestCase):
    """Test the public behavior of OrderQueue."""

    def test_fifo(self):
        """Check that the first item added is removed first."""
        queue = OrderQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")

        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), "A")
        self.assertEqual(queue.dequeue(), "B")
        self.assertEqual(queue.dequeue(), "C")
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)

    def test_peek(self):
        """Check that peek returns the front item without removing it."""
        queue = OrderQueue()
        queue.enqueue("A")
        queue.enqueue("B")

        self.assertEqual(queue.peek(), "A")
        self.assertEqual(queue.peek(), "A")
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), "A")

    def test_empty_and_reuse(self):
        """Check empty operations and reuse after removing all items."""
        queue = OrderQueue()

        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        self.assertIsNone(queue.dequeue())
        self.assertIsNone(queue.peek())

        queue.enqueue("A")
        self.assertEqual(queue.dequeue(), "A")
        self.assertIsNone(queue.dequeue())

        queue.enqueue("B")
        queue.enqueue("C")
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), "B")
        self.assertEqual(queue.dequeue(), "C")

class TestStoreIntegration(unittest.TestCase):
    """Test checkout, processing, and history working together in Store."""
 
    def setUp(self):
        """Create a store with two products and two customers."""
        self.store = Store()
        self.mouse = Product("P1", "Mouse", 10)
        self.keyboard = Product("P2", "Keyboard", 20)
        self.store.add_product(self.mouse)
        self.store.add_product(self.keyboard)
 
        self.ann = Customer("C1", "Ann")
        self.bob = Customer("C2", "Bob")
        self.store.add_customer(self.ann)
        self.store.add_customer(self.bob)
 
    def test_checkout(self):
        """Check that checkout creates an order, queues it, and clears the cart."""
        cart = self.ann.get_cart()
        cart.add_product(self.mouse)
        cart.add_product(self.keyboard)
 
        order = self.store.checkout("C1")
 
        self.assertIsInstance(order, Order)
        self.assertIs(order.get_customer(), self.ann)
        self.assertEqual(order.calculate_total(), 30)
        self.assertEqual(order.get_status(), "PENDING")
        self.assertTrue(cart.is_empty())
        self.assertEqual(self.store.get_orders(), [order])
        self.assertIs(self.store.find_order(order.get_id()), order)
        self.assertIsNone(self.store.find_order("missing"))
 
        # An empty cart and an unknown customer both return None.
        self.assertIsNone(self.store.checkout("C1"))
        self.assertIsNone(self.store.checkout("missing"))
        self.assertEqual(len(self.store.get_orders()), 1)
 
    def test_processing(self):
        """Check that orders are processed oldest first."""
        self.assertIsNone(self.store.process_next_order())
 
        self.ann.get_cart().add_product(self.mouse)
        first = self.store.checkout("C1")
        self.bob.get_cart().add_product(self.keyboard)
        second = self.store.checkout("C2")
 
        self.assertNotEqual(first.get_id(), second.get_id())
 
        self.assertIs(self.store.process_next_order(), first)
        self.assertEqual(first.get_status(), "PROCESSING")
        self.assertEqual(second.get_status(), "PENDING")
 
        self.assertIs(self.store.process_next_order(), second)
        self.assertEqual(second.get_status(), "PROCESSING")
        self.assertIsNone(self.store.process_next_order())
 
    def test_history(self):
        """Check that history is newest first and does not change the stack."""
        self.assertEqual(self.store.get_order_history(), [])
 
        self.ann.get_cart().add_product(self.mouse)
        first = self.store.checkout("C1")
        self.bob.get_cart().add_product(self.keyboard)
        second = self.store.checkout("C2")
 
        # Waiting orders are not part of the history yet.
        self.assertEqual(self.store.get_order_history(), [])
 
        self.store.process_next_order()
        self.store.process_next_order()
 
        self.assertEqual(self.store.get_order_history(), [second, first])
        # Calling it again gives the same result, so nothing was removed.
        self.assertEqual(self.store.get_order_history(), [second, first])
        self.assertEqual(self.store.processed.size(), 2)
 
if __name__ == "__main__":
    unittest.main()