# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        p1 = head
        p2 = head.next

        while p2:
            p1 = p1.next
            
            if p2.next:
                p2 = p2.next.next
            else:
                p2 = p2.next
        
        
        return p1