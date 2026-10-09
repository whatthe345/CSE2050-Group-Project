from node import Node


class LinkedList:
    """Store items in connected nodes with head and tail references."""

    def __init__(self):
        """Create an empty linked list."""
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self, item):
        """Add an item to the beginning of the list."""
        new_node = Node(item, self._head)
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._size += 1
    def __iter__(self):
        """Iterate over the items from first to last without modifying the list."""
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
    def add_last(self, item):
        """Add an item to the end of the list."""
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def remove_first(self):
        """Remove and return the first item, or None if empty."""
        if self.is_empty():
            return None

        item = self._head.data
        self._head = self._head.next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return item

    def get_first(self):
        """Return the first item without removing it, or None if empty."""
        if self.is_empty():
            return None

        return self._head.data

    def is_empty(self):
        """Return whether the list has no items."""
        return self._size == 0

    def size(self):
        """Return the number of items in the list."""
        return self._size