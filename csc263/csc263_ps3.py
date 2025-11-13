'''
CSC263 Winter 2025
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any additional "import" statements
from math import floor

#############################################
# Hash table
###############################################

# Placeholder for a deleted element
DELETED = "DELETED"


# Element in the HashTable
class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v


class HashTable(object):
    """
    A hash table object. Each hash table will have the
    following fields:
        array:    The address table, represented as a list in Python.
                  The values of this address table is either None,
                  DELETED, or a Node object
        capacity: The current size of the address table
        size:     The number of elements in the table.
    """

    def __init__(self, initial_capacity=10):
        # Hash table capacity
        self.capacity = initial_capacity
        self.initial_capacity = initial_capacity

        # Initialize the address table to have all "None"
        # This table should have elements None, "DELETED", or a Node object
        self.array = [None] * initial_capacity

        # Track the number of elements in the hash table
        self.size = 0

    def hash(self, k, capacity=None):
        """
        Hash function that returns a bucket {0, 1, 2, ..., capacity-1} given
        a key `k`. The argument `capacity` is initialized to `self.capacity`,
        but an alternative capacity can be provided.

        This function is provided to you.
        """
        A = 0.6387390215
        if capacity is None:
            capacity = self.capacity
        return floor(capacity * (hash(k) * A % 1))

    def insert(self, k, v):
        """
        Insert Node(k, v) into the hash table. Use the hash function self.hash(),
        and quadratic probing if the slot is already occupied.

        If the key `k` already exists in the Hash Table, replace the corresponding
        value `v`.

        If the hash table capacity is >= 50%, double the hash table capacity.
        """
        i = 0
        while i != self.capacity:

            q = (self.hash(k) + i ** 2) % self.capacity
            if not self.array[q] or self.array[q] == DELETED:
                self.array[q] = Node(k, v)
                self.size += 1
                break

            elif isinstance(self.array[q], Node) and self.array[q].key == k:
                self.array[q].val = v
                break
            i += 1

        if self.size >= self.capacity * 0.5:
            self.resize(self.capacity * 2)

    def search(self, k):
        """
        Return the value of the node with key k in the hash table,
        or None if no such node exists.
        """
        i = 0
        q = (self.hash(k) + i ** 2) % self.capacity
        while self.array[q] and i != self.capacity:

            if isinstance(self.array[q], Node) and self.array[q].key == k:
                return self.array[q].val

            i += 1
            q = (self.hash(k) + i ** 2) % self.capacity

        return None

    def delete(self, k):
        """
        Delete the node with key `k` from the hash table, if it exists.

        If the hash table capacity is <= 25%, halve the hash table capacity,
        but do not go below self.initial_capacity
        """
        i = 0
        q = (self.hash(k) + i ** 2) % self.capacity
        while self.array[q] or i != self.capacity:

            if isinstance(self.array[q], Node) and self.array[q].key == k:
                self.array[q] = DELETED
                self.size -= 1
                break

            i += 1
            q = (self.hash(k) + i ** 2) % self.capacity

        # fails first test case otherwise q.q
        if self.size <= self.capacity * 0.25 and self.capacity > self.initial_capacity:
            self.resize(max(self.initial_capacity, self.capacity * 0.5))

    # You may write helper functions freely
    def resize(self, c):
        """
        Resize the hashtable to capacity c
        """
        arr = self.array

        # Hash table capacity
        self.capacity = c

        # Initialize the address table to have all "None"
        # This table should have elements None, "DELETED", or a Node object
        self.array = [None] * c
        self.size = 0

        for item in arr:
            if isinstance(item, Node):
                self.insert(item.key, item.val)
                # DELETED is to ensure linear probing is done correctly but after resizing we don't need these DELETED nodes anymore


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == "__main__":
    T = HashTable(5)
    T.insert(1, "c")
    T.delete(1)
    # check that the DELETED token is used
    assert T.array[T.hash(1)] == DELETED

    T.insert(1, "c")
    T.insert(2, "s")

    # check that size and capacity are tracked correctly
    assert (T.size == 2)
    assert (T.capacity == 5)

    T.insert(3, "c")

    # check that size and capacity are tracked correctly
    assert (T.size == 3)
    assert (T.capacity == 10)

    # check that search gives us the appropriate result
    n = T.search(1)
    assert (n == "c")
