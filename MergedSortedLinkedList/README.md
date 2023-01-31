### Question
- You are given the heads of two sorted linked lists list1 and list2.
- Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
- Return the head of the merged linked list.
[Link to question.](https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1)

### Thoughts
- Input: 2 sorted linked lists.
- Output: the head of the merged sorted linked list.
- Questions:
    - Can either or both of the linked lists be empty? Yes.
    - Will there be duplicated values? Yes.
- We determine the head of the merged linked list by checking the head of both linked list. Whichever has smaller value will be the head.
- Go through both linked lists at the same time and compare the value at the current position. Take whichever smaller (or equal), then move the pointer of that linked list one up. Once we reach the end of one linked list, just appened the rest of the other linked list to the result linked list and return the head.
- Example: list1: 1->2->4. list2: 1->3->4
    - Compare the head of each linked list. 1 <=1, so take the head of list1 as the head of the merged linked list. 
    - Moved 1 position up at linked list 1 (at 2)
    - Compare list1.curr.val = 2 to list2.curr.val = 1. 1 < 2. Append 1 to the merged linked list (1->1). Move 1 up at linked list 2.
    - Compare list1.curr.val = 2 to list2.curr.val = 3. 2 < 3. Append 2 to the merged linked list (1->1->2). Move 1 up at linked list 1.
    - Compare list1.curr.val = 4 to list2.curr.val = 3. 3 < 4. Append 3 to the merged linked list (1->1->2->3). Move 1 up at linked list 2.
    - Compare list1.curr.val = 4 to list2.curr.val = 4. 4 <= 4. Append 4 to the merged linked list (1->1->2->3->4). Move 1 up at linked list 1.
    - Reached the end of linked list 1. Append the rest of linked list 2 to the merged linked list (1->1->2->3->4->4). Return head.

### Pseudocode
- If linked list 1 is empty return linked list 2 and vice versa.
- Initializing variables:
    - Compare the head of the 2 linked list: Assign head to the one with smaller value.
    - Assign a pointer (sorted_curr) to traverse through the merged linked list.
    - Assign a pointer (l1_curr) to traverse through linked list 1.
    - Assign a pointer (l2_curr) to traverse through linked list 2.
- While we have not reached the end of either linked list:
    - Compare the current value of each linked list.
    - Take the one with smaller value to append to the merged linked list.
    - Move one up from the linked list we just took value from.
- Append the rest of the other linked list that we have not reached the end.
- Return head.
### BigO
- Go through both linked lists to get the final merged linked list => O(M+N) with M being th length of the first linked list, N being the length of the 2nd linked list.

