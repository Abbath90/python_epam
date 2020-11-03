from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result = 0
    for i in nums[:k]:
        result += i
    temp_sum = result
    for i, j in enumerate(nums[k : len(nums)]):
        temp_sum += j - nums[i]
        result = max(result, temp_sum)

    return result
