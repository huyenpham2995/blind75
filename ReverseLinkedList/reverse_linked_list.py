# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        pre = None
        nxt = head.next

        while nxt is not None:
            head.next = pre
            pre = head
            head = nxt
            nxt = head.next
        
        head.next = pre
        return head