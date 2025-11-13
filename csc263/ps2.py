'''
CSC263 Winter 2025
Problem Set 2 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements

###############################################
# BST Nodes.
###############################################

class Node(object):
    """
    A binary tree node object. Each node will have three fields:
        key:   the key stored in the node (a number)
        left:  the left subtree (a Node or None)
        right: the right subtree (a Node or None)

    Do not change this class
    """

    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def range_sum_bst(root: Node, low: int, high: int) -> int:
    """
    Return the sum of the node values within the specified range.

    """
    # todo
    if root is None:
        return 0
    else:
        sum = 0
        if root.key in range(low, high + 1):
            sum += root.key

        if low < root.key:
            sum += range_sum_bst(root.left, low, high)

        if high > root.key:
            sum += range_sum_bst(root.right, low, high)

        return sum


if __name__ == "__main__":
    # Simple test case for range_sum_bst

    # Using the "Node" to represent the binary tree:
    #          5
    #         ---
    #       2   9
    #   1   3

    # Calling range_sum_bst(root, 3, 9) should return the sum of the values 3, 5, and 9
    """
    example_bst = Node(5)
    example_bst.left = Node(2)
    example_bst.left.left = Node(1)
    example_bst.left.right = Node(3)
    example_bst.right = Node(9)
    assert (17) == range_sum_bst(example_bst, 3, 9)

    assert (0) == range_sum_bst(None, 3, 9)

    example_bst = Node(5)
    assert (5) == range_sum_bst(example_bst, 3, 9)

    example_bst = Node(10)
    assert (0) == range_sum_bst(example_bst, 3, 9)

    example_bst = Node(5)
    example_bst.left = Node(3)
    example_bst.right = Node(7)
    assert (15) == range_sum_bst(example_bst, 3, 7)

    example_bst = Node(10)
    example_bst.left = Node(5)
    example_bst.left.left = Node(3)
    example_bst.left.right = Node(7)
    example_bst.right = Node(15)
    example_bst.right.right = Node(18)
    assert (32) == range_sum_bst(example_bst, 7, 15)

    assert (58) == range_sum_bst(example_bst, 1, 20)
    """