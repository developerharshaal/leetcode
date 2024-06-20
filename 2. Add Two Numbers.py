# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        newHead = ListNode(-1)
        ans = newHead
        carry = 0

        while t1 or t2:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            s = val1 + val2 + carry

            carry = s//10
            ans.next = ListNode(s % 10)
            ans = ans.next

            if t1: t1 = t1.next
            if t2: t2 = t2.next

        if carry:
            ans.next = ListNode(1)

        return newHead.next
