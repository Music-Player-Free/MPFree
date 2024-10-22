class ListNode:
    '''
    Class for Doubly Linked List.
    '''
    def __init__(self,key="", val=-1, prev:'ListNode' = None, next:'ListNode' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    # to be used on node to be popped 
    def pop(self) -> None:
        next_node, prev_node = self.next, self.prev
        next_node.prev, prev_node.next = prev_node, next_node
        return

    # to be used on head of list (insertion point)
    def insert(self, node: 'ListNode'):
        next_node = self.next
        self.next, node.prev = node, self
        next_node.prev, node.next = node, next_node

class LRU_Cache:
    '''
    Class for Least Recently Used Cache.
    '''
    def __init__(self, capacity:int = 20):
        # Init hashmap of keys for O(1) lookup
        self.map = {}

        # Establish capacity of LRU 
        self.capacity = capacity

        # Create head and tail of DLL
        self.head = ListNode()
        self.tail = ListNode()

        # Point them to eachother
        # head<->tail
        self.head.next, self.tail.prev = self.tail, self.head

    # not sure about the types of these vars
    def put(self, key: int, value: int):
        ''' 
        Put operation.\n
        Adds key to LRU cache if not already present, else pops the key node and inserts to front.
        '''
        if key in self.map:
            # Point to node
            node: 'ListNode' = self.map[key]
            # Remove from hmp
            del self.map[key]
            # Free from list (point surrounding nodes to eachother)
            node.pop()

        if len(self.map) == self.capacity:
            # Tail points to node that hasn't been accessed the longest and should be popped to make room

            del self.map[self.tail.prev.key] # Remove from hmp 
            self.tail.prev.pop() # Free from list (will be garbage collected)

        # create new list
        node = ListNode(key, value)
        # Add to hmp
        self.map[key] = node
        self.head.insert(node)

        

    def get (self, key):
        '''
        Get operation.\n
        Returns value of key if present, or -1 if not.
        '''
        # If key present, point to node, reinsert and return value.
        if key in self.map:
            node: 'ListNode' = self.map[key]
            node.pop()
            self.head.insert(node)
            return node.val
        # If not present, return -1
        return -1
        