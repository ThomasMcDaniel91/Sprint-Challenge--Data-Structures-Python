"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.right = BSTNode(value)

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checks to see if the target is the root node
        if self.value == target:
            return True
        # otherwise we check to see it's value compared to the target
        # to determine which way to go to find the target
        else:
            if self.value <= target:
                if self.right:
                    # if the target is higher than the value, go right recursively with the self.right
                    # as the new parameter with the target
                    return self.right.contains(target)
                else:
                    # if target is higher than value and there is no right node
                    # then the target does not exist in the tree and returns false
                    return False
            if self.value >= target:
                if self.left:
                    #if target is smaller and there is a self.left node then check again
                    # with self.left and the target
                    return self.left.contains(target)
                else:
                    # if the target is lower and there is no left node then the target
                    # cannot exist in the tree, so we return false
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # check to see if there is a higher value to the right of current one
        if self.right is None:
            # if there is none that means we have the highest value, returns that
            return self.value
        else:
            # otherwise, we run the function again on the right child node
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # runs the function on the root node
        fn(self.value)
        # if there is a value to the left, run it again on that node
        if self.left:
            self.left.for_each(fn)
        # if there is a value to the left, run it on that node as well
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        if self.right:
            self.right.in_order_print()
        else:
            print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  