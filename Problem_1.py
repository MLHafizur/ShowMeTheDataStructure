from collections import OrderedDict


class LRU_Cache(OrderedDict):

    def __init__(self, capacity: int = 5):
        self.capacity = capacity

    def set(self, key, value):
        # If cache at capacity, pop the least-recent item
        if len(self) >= self.capacity:
            self.popitem(last=False)
        
        # If key is present, reset to track access order
        if key in self:
            del self[key]
        self[key] = value

    def get(self, key):
        # OrderedDict will raise a KeyError if key not present
        # Handle this behavior
        try:
            value = self[key]
            
            # Reset key, value pair to track access order
            del self[key]
            self[key] = value 

            return value
        except:
            return -1


if __name__ == '__main__':
    our_cache = LRU_Cache(5)

    # Fill cache
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # Test behavior when returning existing keys
    print(our_cache.get(1)) # should print 1
    print(our_cache.get(2)) # should print 2

    # Test behavior for unset keys
    print(our_cache.get(9)) # should print -1

    # Fill cache so that LRU falls out
    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    # Test expected beahvior for least recent value
    print(our_cache.get(3)) # should print -1


    # Empty Cache
    cache_2 = LRU_Cache()

    # Cache capacity should initialize to 5
    print(cache_2.capacity)

    # Should return -1 for missing value
    print(cache_2.get(1))


    # Test insertion of non-integer values
    cache_3 = LRU_Cache(capacity=2)

    cache_3.set('a', 1)
    cache_3.set('b', 2)
    cache_3.set('c', 3)

    # Should return 3
    print(cache_3.get('c'))

    # Should return -1, as value fell out when at capacity
    print(cache_3.get('a'))
