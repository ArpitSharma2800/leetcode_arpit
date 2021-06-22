# 152. Maximum Product Subarray
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

from typing import List


def maxProduct(nums: List[int]) -> int:
    result = max(nums)
    mini, maxi = 1, 1

    for n in nums:
        if n == 0:
            mini, maxi = 1, 1
            continue
        tmp = n * maxi
        maxi = max(n * maxi, n * mini, n)
        mini = min(tmp, n * mini, n)
        result = max(result, maxi)
    return result
