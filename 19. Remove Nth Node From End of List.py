# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next

        if n == cnt:
            return head.next

        res = cnt - n
        temp = head
        while temp:
            res -= 1
            if res == 0: break
            temp = temp.next
        temp.next=temp.next.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n): fast = fast.next
        
        if fast == None: return head.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        

        slow.next = slow.next.next
        return head
