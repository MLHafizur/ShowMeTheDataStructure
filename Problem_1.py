class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.bucket_array = [None] * (capacity + 1)
        self.num_of_elements = 0
        self.queue = []
    def get(self, key):
        if len(self.bucket_array) == 1: #capacity is zero
            return -1
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key > len(self.bucket_array):
            return -1
        if self.bucket_array[key] != None:
            self.num_of_elements -=1 
            if self.queue[0] == key: 
                self.queue.append(self.queue.pop(0))
            return self.bucket_array[key]
        else:#collision
            return -1

    def set(self, key, value):
        if len(self.bucket_array) == 1:
            print("Warnning: cannot perform operations on 0 capacity cache")
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key < len(self.bucket_array) and  self.bucket_array[key] == None:
            self.bucket_array[key] = value
            self.num_of_elements += 1
            self.queue.append(key)
        else:#cache full
            oldest = self.queue.pop(0)
            self.bucket_array[oldest] = None
            self.bucket_array.extend([None])
            self.bucket_array[key] = value


# Test1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
#print(our_cache.tail.data)   
#print(our_cache.head.data)   

print(our_cache.get(1))       
# expected output: 1
print(our_cache.get(2))    
# expected output: 2
print(our_cache.get(9))        
# expected output: -1 

#print(our_cache.tail.data)
#print(our_cache.head.data)
our_cache.set(5, 5) 
our_cache.set(6, 6)
#print(our_cache.tail.data)
#print(our_cache.head.data)

print(our_cache.get(3))    
# expected output: -1 
print(our_cache.get(6))    
# expected output: 6
print(our_cache.get(1))    
# expected output: 1

print('\n-----------------------------------\n')

#Test 2
our_cache = LRU_Cache(3)
our_cache.set(0, 0)
our_cache.set(1, 1)
our_cache.set(2, 2)

our_cache.set(1, 10)
our_cache.set(0, 5)
our_cache.set(2, 17)

print(our_cache.get(0))
# expected output: 5
print(our_cache.get(1))
# expected output: 10
print(our_cache.get(2))
# expected output: 17

print('\n-----------------------------------\n')

#Test 3
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# expected output: "Can't perform operations on 0 capacity cache"
print(our_cache.get(17))
# expected output: -1

