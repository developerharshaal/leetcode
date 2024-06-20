# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head is None and head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def findK(self, temp, k):
        k -= 1
        while temp and k>0:
            temp = temp.next
            k -= 1
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = ListNode(None)
        while temp:
            kthNode = self.findK(temp, k)
            if kthNode == None:
                if prevNode: prevNode.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode

        return head

        
