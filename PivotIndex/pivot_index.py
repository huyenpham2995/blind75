from typing import List

def find_pivot_index(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums) -1
    
    lsum = 0
    rsum = sum(nums)

    for i in range(len(nums)):
        if i!=0:
            lsum += nums[i-1]
        rsum -= nums[i]
        if lsum == rsum:
            return i
    
    return -1