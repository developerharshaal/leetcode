"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        temp = head
        mpp ={}
        while temp:
            newNode = Node(temp.val)
            mpp[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            copy = mpp[temp]
            copy.next = mpp.get(temp.next)
            copy.random = mpp.get(temp.random)
            temp = temp.next
        return mpp[head]
        return head



    

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def func(self, head):
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next
        return array

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp = head
        while temp:
            new = Node(temp.val)
            nex = temp.next
            new.next = nex
            temp.next = new
            temp = temp.next.next
        
        temp = head
        while temp:
            copy = temp.next
            if temp.random: copy.random = temp.random.next
            else: copy.random = None
            temp = temp.next.next

        new = Node(-1)
        res = new
        temp = head
        while temp:
            res.next = temp.next
            temp.next = temp.next.next

            res = res.next
            temp = temp.next

        return new.next
