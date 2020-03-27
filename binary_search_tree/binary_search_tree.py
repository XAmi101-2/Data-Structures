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
        #looks to see if node value is greater than self.value, is so recurse left
        if value < self.value:
            #if so go left side and check if the left is empty
            if self.left is None:
                #if so the node value then becomes the new value and return it 
                self.left = BinarySearchTree(value)
                return
            else:
                #but if there is a value then inserts the value in the left node
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
        # check/compare if the node is empty
        # check/compare if the node value is the same as target search value
            # return true
        # else if target search value is less than the node value (go left ) and if there is node.left  
            # return  the left side contains the target
        # else if target is  greater than the tree value recurse right and if there is node.right 
            # return  the right side contains the target
        ## else return false
        
        if self.value == None:
            return False
        if self.value == target:
            return True
        # elif target < self.value and self.left :
            #  return self.left.contains(target)
        # elif self.right and target > self.value:
        #     return self.right.contains(target)
        elif target < self.value:
            if self.left:
                return self.left.contains(target)   
        elif target > self.value:
            if self.right:
                return self.right.contains(target)   
        # else:
        #     return False

    # Return the maximum value found in the tree
    def get_max(self):
        # PLAN
        # check if there is a value on the right 
            # if so return get max value on right
        # else return node.value

        if self.right:
            return self.right.get_max()
        else:
            return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #PLAN
        #call CB on self.value
        #if left 
            #call for_each
        #if right            
            #call for_each

        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # PLAN
        #if node is not None:
            # Check left aka do recursive call with node.left, that has the smallest number
                # print(node.value)
            # do recursive call with node.right
                 # print(node.value)

        if self.value != None:
            if self.left:
                self.left.in_order_print(node)
            if self.right:
             self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        #PLAN
        #create/initialize queue
        #add root to queue
        #while queue is not empty
            #pop head/top item out of queue & into temp variable  [node = pop head of queue]
            #if temp exists  
                # if there is temp var on the right 
                    #put that into the queue on the right
                # if there is a left temp var   
                    #put that into the queue on the left
                # DO the THING!... print temp value
            # else break
                
        queue = Queue()
        queue.enqueue(node)
        while queue.len != 0:
            temp: BinarySearchTree = queue.denqueue()
            if temp:
                if temp.right:
                    queue.enqueue(temp.right)
                if temp.left:
                    queue.enqueue(temp.left)
                print(temp.value)
            else:
                break

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #PLAN
        #create/initialize stack
        #add/push root to stack
        #while stack is not empty
            #pop head/top item out of stack & into temp variable  [node = pop head of stack]
            #if temp exists  
                # if there is temp var on the right 
                    #put that into the stack on the right
                # if there is a left temp var   
                    #put that into the stack on the left
                # DO the THING!... print temp value
            # else break

        stack = Stack()
        stack.push(node)
        while stack.len != 0:
            temp: BinarySearchTree = stack.pop()
            if temp:
                if temp.right:
                    stack.push(temp.right)
                if temp.left:
                    stack.push(temp.left)
                print(temp.value)
            else:
                break

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
