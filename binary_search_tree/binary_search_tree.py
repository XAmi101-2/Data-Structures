import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # PLAN
        #looks to see if node value is greater than self.value, is so go left
        if value < self.value:
            #if so go left side and check if the left is empty
            if self.left is None:
                #if so the node value then becomes the new value and return it 
                self.left = BinarySearchTree(value)
                return
            else:
                #but if there is a value then inserts the node in the left 
                self.left.insert(value)

        #But if node value is less than or equal to self.value
        if value >= self.value:
            #go right and check if the right side is empty
            if self.right is None:
                #if so node value becomes the new value for the right
                self.right = BinarySearchTree(value)
                return
            else:
                #but if there is a value then it inserts it in the right side
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # PLAN
        # check if the self value is the same as target
            # return true
        # else if the tree value is the greater than the value in the left and target
            # return that the left side contains the target
        # else if the tree value is the less than the value in the right and target
            # return that the right side contains the target
        # else return false

        if self.value == target:
            return True
        elif self.left and target < self.value:
            return self.left.contains(target)
        elif self.right and target > self.value:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
