from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #Plan
        #limits the amt of nodes cache can hold to 10
        #show current number of nodes it has
        #variable used to set the value being set by Doublylinked list, a list that holds the key-value entries
        #dictionary for access (hash table) s well as a storage dict that provides fast access to every node stored in the cache.
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # plan if there is a key in storage, 
        # move to the front, then refresh the order and return the value which is a truple, 
        # else return none
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None
            
       

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # PLAN VER.2 reformulated
         # check and see if the key is in the dict
        if key in self.storage:
             # if it is, THEN GRAB A NEW NODE WITH THE KEY,VALUE PAIR AND STORE IT INT HE DICTIONARY
            node = self.storage[key]
             # overwrite the value  AND KEEP THE KEY VALUE PAIR          
            node.value = (key, value)  # OR self.value=[key:value]
             # move it to the front (OR END, IT'S MY CHOICE )
            self.order.move_to_front(node)
             # NOTHING ELSE TO DO SO WE EXIT THE FUNCTION
            return

        # if it isn't, check and see if cache is  full       
        if self.size is self.limit:
             # if cache is full remove oldest entry from the dictionary (which is the OPPOSITE OF LINE 71,
            """( if the node in 71 was moved to the end the line 80 below would be ~.head.value[0] because in line 69 [0] is where we stored the key)"""                     
            del self.storage[self.order.tail.value[0]] # OR self.value=[self.order.tail.value.key] when other version on line 69  is done.
             # ALSO remove that entry from the Linked list
            self.order.remove_from_tail()  
             # reduce size
            self.size -= 1
            
         # Update cahce and ADD the new entry  to the linked list (key and value)
        self.order.add_to_head((key, value))
         # Add the Key and value o the dictionary
        self.storage[key] = self.order.head
         # increment 
        self.size += 1



        
        # Plan
        # if  cache is not empty 
            # check and see if the key is in the dict
                # if it is
                    # overwrite the value
                    # move it to the end
                # if it isn't
                    # check and see if cache is  full
                        # if cache is not full
                            # same as if cache is empty
                        # if cache is full
                            # remove olderest entry from the dictionay
                            # and remove that entry from the Linkeded list also
                            # reduce size
                            # same as if cache is empty ; update cahce and add the new entry
        # IF THE CACHE IS EMPTY
            # Add to the linked list (key and value)
            # Add the Key and value o the dictionary
            # increment  
        

        # PLAN VER.2 reformulated
            # check and see if cache is  full
                # if it is
                    # overwrite the value
                    # move it to the end
                 # if it isn't
                    # check and see if the key is in the dict
                        # if cache is not full
                            # same as if cache is empty
                        # if cache is full
                            # remove olderest entry from the dictionay
                            # and remove that entry from the Linkeded list also
                            # reduce size
                            # same as if cache is empty ; update cahce and add the new entry

            # Add to the linked list (key and value)
            # Add the Key and value o the dictionary
            # increment  
