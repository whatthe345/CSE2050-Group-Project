from linked_list import LinkedList


class OrderQueue:
    """Store items in first-in, first-out order using a linked list."""

    def __init__(self):
        """Create an empty queue."""
        self._items = LinkedList()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.add_last(item)

    def dequeue(self):
        """Remove and return the front item, or None if empty."""
        return self._items.remove_first()

    def peek(self):
        """Return the front item without removing it, or None if empty."""
        return self._items.get_first()

    def is_empty(self):
        """Return whether the queue has no items."""
        return self._items.is_empty()

    def size(self):
        """Return the number of items in the queue."""
        return self._items.size()