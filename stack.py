from linked_list import LinkedList


class Stack:
    """Store items in last-in, first-out order using a linked list."""

    def __init__(self):
        """Create an empty stack."""
        self._items = LinkedList()

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.add_first(item)

    def pop(self):
        """Remove and return the top item, or None if empty."""
        return self._items.remove_first()

    def peek(self):
        """Return the top item without removing it, or None if empty."""
        return self._items.get_first()

    def is_empty(self):
        """Return whether the stack has no items."""
        return self._items.is_empty()

    def size(self):
        """Return the number of items in the stack."""
        return self._items.size()


stack = Stack()
stack.push("A")
stack.push("B")

print(stack.peek())  # B — stays in the stack
print(stack.pop())   # B — removed
print(stack.pop())   # A — removed
print(stack.pop())   # None — stack is empty