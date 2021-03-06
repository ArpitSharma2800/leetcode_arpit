# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
from typing import List


def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    sum = 0
    for i in nums:
        if sum < 0:
            sum = 0
        sum = sum + i
        maxSub = max(maxSub, sum)
    return maxSub


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
