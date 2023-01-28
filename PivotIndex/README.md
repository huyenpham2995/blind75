### Question
- Given an array of integers nums, calculate the pivot index of this array.
- The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
- If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
- Return the leftmost pivot index. If no such index exists, return -1.
[Link to question.](https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: array of integers (nums)
    - Output: the index of the pivot.
- If the array don't have any element, then return -1 (no pivot found).
    - Special case in python: -1 is the index of the last element in the array. Since we use -1 as the "invalid" index, the last element can only be referred to as len(array)-1
- If the array has 1 element, return 0 (that element is the pivot, since left sum = right sum = 0).
Example: nums = [1,7,3,6,5,6], output: 3.
- Approach 1: can go through each element and pretend they are the chosen pivot. Calculate the left sum (lsum) and right sum (rsum). If lsum=rsum then return the index of the current element, if we go through the whole array and lsum!=rsum then return -1.
    - At i=0: lsum = 0, rsum = 7+3+6+5+6 = 27. i=-1. Reset lsum and rsum.
    - At i=1: lsum = 1, rsum = 3+6+5+6 = 20. i=-1. Reset lsum and rsum.
    - At i=2: lsum = 1+7 = 8, rsum = 6+5+6 = 17. i=-1. Reset lsum and rsum.
    - At i=3: lsum = 1+7+3 = 11, rsum = 5+6 = 11 => return i=3
- Approach 2: looking at approach 1, every time we calculate rsum and lsum, we do duplicate works. For example, at i=3, lsum = nums[0] + nums[1] + nums[2]. But nums[0] + nums[1] is already calculated at i=2, it's simply just take (lsum at i=2) + nums[2]. Same with rsum at i=3, we just need to take (rsum at i=2) - nums[3]. So the steps become:
    - At i=0: lsum = 0, rsum = sum(nums) - nums[0]
    - At i=1: lsum += nums[0], rsum -= nums[1]
    - At i=2: lsum += nums[1], rsum -= nums[2]
    ...

### Pseudocode
function find_pivot_index
- if nums has 0 element, return -1.
- if nums has 1 element, return 0.
- Initialize variables 
    - lsum = 0
    - rsum = sum(nums)
- Loop through the nums list
    - if i!=0 (not the first element): lsum += nums[i-1]
    - rsum -= nums[i]
    - if lsum == rsum:
        return i //this will make sure we get the leftmost, i.e the first pivot index.
- Run through the loop and no pivot index found: return -1.

### BigO
- For the first approach, aside from looping through the whole nums array size N, at each element, we loops through all elements on the left to calculate lsum and all elements on the right to calculate rsum (N-1 elements) => O(N^2).
- For the 2nd approach, we reuse the calculation of the previous element, so for each element, calculate lsum takes 1 step, rsum takes 1 step. We loop through N elements => O(N).
    - Calculating the sum of the array take N steps (to loop through the array), but that's not in the loop => O(2N) = O(N).