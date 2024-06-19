# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        st = []
        temp = head
        while temp:
            st.append(temp.val)
            temp = temp.next
        st.sort()
        temp = head
        i = 0
        while temp:
            temp.val = st[i]
            i += 1
            temp = temp.next

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self, head):
        if head is None or head.next is None:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, ll1, ll2):
        dummy = ListNode()
        temp = dummy
        while ll1 and ll2:
            if ll1.val < ll2.val:
                temp.next = ll1
                temp = ll1
                ll1 = ll1.next
            else:
                temp.next = ll2
                temp = ll2
                ll2 = ll2.next
        if ll1: temp.next = ll1
        else: temp.next = ll2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        middle = self.middle(head)
        right = middle.next
        middle.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
