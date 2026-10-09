import unittest

from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue


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


if __name__ == "__main__":
    unittest.main()