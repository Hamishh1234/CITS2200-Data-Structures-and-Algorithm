class Heap:
    """A basic heap.

    You may use whatever implementation you like, though a leftist binary heap
    is probably easiest to implement.
    """

    def __init__(self, items=[], key=None, reverse=False):
        """Constructs a Heap.

        Target Complexity: O(N)

        Args:
            items: Optional. The initial contents of the heap.
            key: Optional. A function to extract a comparison key from an item.
            reverse: Optional. True for a max-heap, False otherwise.
        """
        pass

    def __len__(self):
        """Returns the number of elements in the Heap."""
        pass

    def push(self, item):
        """Insert the given item into the Heap.

        Target Complexity: O(lg N).

        Args:
            item: The item to insert.
        """
        pass

    def peek(self):
        """Returns the top element of the Heap.

        Target Complexity: O(1).

        Returns:
            The topmost element in the Heap.

        Raises:
            IndexError: If the Heap is empty.
        """
        pass

    def pop(self):
        """Removes and returns the top element of the Heap.

        Target Complexity: O(lg N).

        Returns:
            The topmost element in the Heap.

        Raises:
            IndexError: If the Heap is empty.
        """
        pass


def heapsort(xs, key=None, reverse=False):
    """Sorts the given list using heapsort.

    Sorts in ascending order by default.

    Args:
        xs: The list to be sorted.
        key: Optional. A function to extract a comparison key from an item.
        reverse: Optional. True for descending order, False for ascending.

    Returns:
        The sorted list.
    """
    pass
