# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = ListNode()
        list1_curr = list1
        list2_curr = list2

        if list1.val <= list2.val:
            head = list1 
            list1_curr = list1.next
        else:
            head = list2
            list2_curr = list2.next

        sorted_curr = head
        while list1_curr and list2_curr:
            if list1_curr.val <= list2_curr.val:
                sorted_curr.next = list1_curr
                list1_curr = list1_curr.next
            else:
                sorted_curr.next = list2_curr
                list2_curr = list2_curr.next
            sorted_curr = sorted_curr.next
        
        if list1_curr:
            sorted_curr.next = list1_curr

        if list2_curr:
            sorted_curr.next = list2_curr
        
        return head