### Question
- Given the head of a singly linked list, return the middle node of the linked list.
- If there are two middle nodes, return the second middle node.
[Link to question.](https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=level-1)

### Thoughts
- Input: a singly linked list.
- Output: the middle node of that list.
- Questions:
    - Can the Linked list be empty? yes.
    - What if there's only 1 node? That node is the middle one.
    - What if there are 2 nodes? The 2nd one is the middle.
- Approach 1: determine the length of the linked list.
    - Traverse till the end of the linked list to count how many nodes it has. The traverse again to the middle and return the middle node.
        - If the list has odd number of nodes, then we need to go floor(length/2) steps to get to the middle node.
        - If the list has even number of nodes, we then walk length/2 step to get to the middle node.
- Approach 2: 2 walkers.
    - First one walks 1 step at a time.
    - 2nd one walks 2 steps at a time.
    - Then by the time the 2nd one walks till the end of the list, the 1st one will stay in the middle.
    - Example: 1,2,3,4,5,6,7.
        - p1 at 1, p2 at 2.
        - p1 at 2, p2 at 4.
        - p1 at 3, p2 at 6.
        - p1 at 4, p2 at None.
        - Stop. Return p1.

### Pseudocode
- Approach 1: We go through the list 1 time to determine its length, then go through half of it the 2nd time => O(N + 1/2N) = O(3/2N) = O(N).
- Approach 2: 2 pointers are moving at the same time. Each of them move N/2 steps (pointer 1 traverses half of the array 1 step at a time, pointer 2 traverse to the end but do that 2 steps at a time) => O(N/2 + N/2) = O(N).
- They have the same bigO but technicall approach 2 is faster, esp when the list grows long.

### BigO

