from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        
        p = head
        count_dict = defaultdict(int)

        while p:
            if count_dict[p] == 0:
                count_dict[p] +=1
            else:   
                return p
            p = p.next
        
        return None