# https://leetcode.com/problems/missing-number/description/
from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    total = n * (n + 1) // 2

    return total - sum(nums)


nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(missing_number(nums1))
print(missing_number(nums2))
print(missing_number(nums3))
