### Question
- Given the head of a singly linked list, return the middle node of the linked list.
- If there are two middle nodes, return the second middle node.
[Link to question.](https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=level-1)

### Thoughts
- Input: a singly linked list.
- Output: the node which cycle occurs. None if there's no cycle.
- Questions:
    - What if the list is empty? No cycle.
    - Will there be duplicated entries in the list? Like 1->2->3->2->4. Yes. So we care more about the location of the cycle than the value at that node.
- If there's a cycle, a value will occur twice. We can create another dictionary to keep track of the address of each node. If we encounter the address again, return that node.

### Pseudocode
#### Approach 1
- If head == None: return None
- Initialize variables:
    - Create a dictionary (count_dict) with default variable 0.
    - p = head
- while p:
    - count_dict[p] += 1
    - if count_dict[p] > 1: return p
    - p = p.next

#### Approach 2
The smart way: 2 pointers. 1 of them going 1 step at a time, the other 2 steps at a time. At a certain point, they will meet each other.

### BigO
- Approach 1: will go through the list N times if there's no loop, N=1 times if there's a loop => O(N+1) = O(N). For space capacity, we need a dictionary of at most N slots (to store N unique nodes), so O(N) with N being the number of nodes in the list.
- Approach 2: same runtime, but O(1) space due to using only 2 pointers, no matter how many nodes there are in the list.

