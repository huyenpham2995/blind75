### Question
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
[Link to question.](https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: array of nums.
    - Output: array of running sum of nums.
- Questions:
    - Can this array be empty? Yes. Return 0 if it's empty.
    - Will I be passed invalid array (i.e: an array of string)? In real life maybe (and should throw exception), but pretend in the scope of this question no.
    - Will there be negative values? Yup.
- Some ways to do it: [1,2,3,4,5]
    - Approach 1: The sum starts off with 0. Travel the array and at each location, sum up whatever number from the beginning to the current number, and save the sum to the result list.
        - At index 0: sum = 0+1 = 1. result_list = [1]. Reset sum to 0.
        - At index 1: sum = 0+1+2 = 3. result_list = [1,3]. Reset sum to 0.
        ...
        - At index 4: sum = 0+1+2+3+4+5 = 15. result_list = [1,3,6,10,15]
        There is better way to do it tho. For example at index 1, the sum is 0+1+2. But the (0+1) part is already done at index 0. We are duplicating our work. The further along the list, the more duplicates that we create.
    - Approach 2: utilize what has been done previously.
        - At index 0: sum = 0+1 = 1. result_list = [1].
        - At index 1: sum += 2 = 3. result_list = [1,3].
        ...   

### Pseudocode
function getRunningSum
    - Check to see the array is empty. If it is return 0.
    - Initialize sum = 0
    - Initialize result_list = []
    - Loop through the array. Let's call the index of the current position i
        - sum = sum + array[i]
        - Append sum to the result_list
    - Return result_list

### BigO
- Approach 1: I go through all the element in the array of size N, at each location I sum up all the numbers from the beginning to current position then continue. At most (at the last element), I need to travel the whole array from the beginning to get the sum. So run time will be N*N => O(N^2).
- Approach 2: go through all the element in the array, at each position calculate the sum by getting previous sum + num at current position => O(N).
