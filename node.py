class Node:
    """Store an item and a reference to the next node."""

    def __init__(self, data, next=None):
        """Initialize the node with data and an optional next node."""
        self.data = data
        self.next = next