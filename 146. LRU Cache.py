from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def add(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def delete(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev        

    def get(self, key: int) -> int:
        if key in self.m:
            res = self.m[key]
            ans = res.val
            del self.m[key]
            self.delete(res)
            self.add(res)
            self.m[key] = self.head.next
            return ans
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.delete(curr)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.delete(self.tail.prev)

        self.add(Node(key, value))
        self.m[key] = self.head.next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
