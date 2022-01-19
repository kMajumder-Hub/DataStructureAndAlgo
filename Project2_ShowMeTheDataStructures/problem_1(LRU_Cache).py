class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.lru_cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.lru_cache:
            return self.lru_cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if not self.capacity or self.capacity <= 0:
            return 'Capacity of your cache is zero or null'
        
        if (len(self.lru_cache) == self.capacity):
            self.lru_cache.pop(list(self.lru_cache.keys())[0])
        self.lru_cache[key] = value
        

    
#Test case 1        
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)                      
print(our_cache.get(3))       # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#Test case 2
our_cache = LRU_Cache(4)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(1, 4)
our_cache.set(4, 5)
our_cache.set(5, 6)
print(our_cache.get(1))  # should return 4
print(our_cache.get(2))  # should return -1 because it is least recently used

#Test case 3 (Edge case)
our_cache = LRU_Cache(0)
our_cache.set(1, 1)      # should print capacity of your cache is zero or null!
our_cache = LRU_Cache()
our_cache.set(1, 1)      # should print capacity of your cache is zero or null!

#Test case 4 (Edge case)
our_cache = LRU_Cache(-1)
our_cache.set(1, 1)      # should print capacity of your cache is zero or null!
