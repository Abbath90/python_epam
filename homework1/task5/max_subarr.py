"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""

from typing import List


def max_of_two(first: int, second: int):
    if first >= second:
        return first
    else:
        return second


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result = nums[0]
    for i, j in enumerate(nums):
        temp_sum = 0
        for _, m in enumerate(nums[i : i + k], i):
            temp_sum += m
            result = max_of_two(result, temp_sum)
    return result
