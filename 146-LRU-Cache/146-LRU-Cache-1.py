class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        # left = LRU, right = most recent
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        #self.cache.pop(node.key, None)

    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # evict least recently used
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key, None)
       

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)