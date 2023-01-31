### Question
- Given the head of a singly linked list, reverse the list, and return the reversed list.
[Link to question.](https://leetcode.com/problems/reverse-linked-list/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: a singly linked list.
    - Output: the head of the reversed linked list.
- Questions:
    - Can the linked list be empty? Yup.
- What do I need to keep track of?
    - The node before my current node. Because it will be my new next.
    - The node next to my current node. I still need to traverse to the next node. 
- Example: 1->2->3:
    - Head is at 1. The new next should be None since head will become the last node after the reversing process. 
    - Move head to 2. The new next should be 1.
    - Move head to 3. The new next should be 2.
    - Reach the end. Return head at 3.

### Pseudocode
#### The iteratively approach
- If head==None: return head
- Initialize variables:
    - pre = None
    - curr = head
    - next = head.next
- While curr is not None:
    - curr.next = pre
    - pre = curr
    - curr = next
    - next = curr.next
- Return pre


### BigO


