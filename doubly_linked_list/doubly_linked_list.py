"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length
        
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        #  If the list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
    
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        #  If the list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        max_value = current.value
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value



#  """ MY NOTES """

    # """Wraps the given value in a ListNode and inserts it 
    # as the new head of the list. Don't forget to handle 
    # the old head node's previous pointer accordingly."""
    # def add_to_head(self, value):
    #     # pass
    #     self.length += 1
    #     if not self.head and not self.tail:
    #         # this is the em,pty list with new head and tail
    #         self.head = self.tail = ListNode(value)
    #     else:
    #         # we know the list is the populated list
    #         self.head.insert_before(value)
    #         self.head = self.head.prev

    # """Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the value of the removed Node."""
    # def remove_from_head(self):
    #     # pass
    #     #current node head
    #     value = self.head.value
    #     #Removes the List's current value
    #     self.delete(self.head)
    #     #returns removed Node value
    #     return value

    # """Wraps the given value in a ListNode and inserts it 
    # as the new tail of the list. Don't forget to handle 
    # the old tail node's next pointer accordingly."""
    # def add_to_tail(self, value):
    #     # pass
    #     self.length += 1
    #     if not self.head and not self.tail:
    #         self.head = self.tail = ListNode(value)
    #     else:
    #         self.tail.insert_after(value)
    #         self.tail = self.tail.next

    # """Removes the List's current tail node, making the 
    # current tail's previous node the new tail of the List.
    # Returns the value of the removed Node."""
    # def remove_from_tail(self):
    #     # pass
    #     value = self.tail.value
    #     newtail = self.tail.prev
    #     self.delete(self.tail)
    #     self.tail = newtail
    #     return value

    # """Removes the input node from its current spot in the 
    # List and inserts it as the new head node of the List."""
    # def move_to_front(self, node):
    #     # if node is self.head:
    #     #     return
    #     # value = node.value
    #     # if node is self.tail
    #     #     self.remove_from_tail  # WHAT DO WE SPEFICALLY WANT TO REMOVE IN remove_from_tail .... the pointers?
    #     # else:
    #     #     node.delete()
    #     # self.add_to_head(value)
    #     #      OR ...
    #     self.delete(node)
    #     self.add_to_head(node.value)

    # """Removes the input node from its current spot in the 
    # List and inserts it as the new tail node of the List."""
    # def move_to_end(self, node):
    #     # pass
    #     self.delete(node)
    #     self.add_to_tail(node.value) #pointer untouched but still there

    # """Removes a node from the list and handles cases where
    # the node was the head or the tail"""
    # def delete(self, node):
    #     # pass
    #     #Planning
    #     # If LL is empty
    #     if not self.head and not self.tail:
    #         print("ERROR:  Attempted to delete node not in list")
    #         return
    #     # If node is both
    #     elif self.head == self.tail:
    #         self.head = None
    #         self.tail = None

    #     # If node is head 
    #     elif node == self.head:
    #         self.head = self.head.next
    #         node.delete()
    #     # If node is tail
    #     elif node == self.tail:
    #         self.tail = self.tail.prev
    #         node.delete()
    #     # If node is in middle
    #     else:
    #         node.delete()
    #     self.length -=1
        
    # """Returns the highest value currently in the list"""
    # def get_max(self):

    #     # Plan:

    #     # Make max var
    #     # Loop through nodes via node.next
    #     # If node.value is higher, update max
    #     # Return max
    #     if not self.head:
    #         return None
    #     max_value = self.head.value
    #     current_node = self.head
    #     while current_node:
    #         if current_node.value > max_value:
    #             max_value = current_node.value
    #         current_node = current_node.next
    #     return max_value

