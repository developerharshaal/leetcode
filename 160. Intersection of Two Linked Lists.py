# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashh = {}
        temp = headA
        while temp:
            hashh[temp] = 1
            temp = temp.next

        temp = headB
        while temp:
            if temp in hashh:
                return temp
            temp = temp.next
        return None


        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m, n = 0, 0
        temp = headA
        while temp:
            m += 1
            temp = temp.next
        temp = headB
        while temp:
            n += 1
            temp = temp.next

        listA, listB = [] , []
        h1, h2 = headA, headB
        d = m - n if m > n else n - m
        if m > n:
            while d:
                h1 = h1.next
                d -= 1
        else:
            while d:
                h2 = h2.next
                d -= 1
        while h1 != h2:
            h1 = h1.next
            h2 = h2.next
        return h1




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is None:
            return None

        t1, t2 = headA, headB
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

            if t1 == t2: return t1
            
            if t1 == None: t1 = headB
            if t2 == None: t2 = headA

        return t1

        
