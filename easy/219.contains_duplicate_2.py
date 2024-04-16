# https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    known_numbers = {}

    for idx, num in enumerate(nums):
        if num not in known_numbers:
            known_numbers[num] = idx
        else:
            if (idx - known_numbers[num]) <= k:
                return True
            else:
                known_numbers[num] = idx

    return False


nums1 = [1, 2, 3, 1]
k1 = 3
nums2 = [1, 2, 3, 1, 2, 3]
k2 = 2

print(contains_nearby_duplicate(nums1, k1))
print(contains_nearby_duplicate(nums2, k2))
