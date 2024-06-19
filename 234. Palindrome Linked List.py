# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = self.reverseLL(slow.next)
        first = head
        second = head2
        while second:
            if first.val != second.val:
                self.reverseLL(head2)
                return False
            first = first.next
            second = second.next

        self.reverseLL(head2)
        return True
