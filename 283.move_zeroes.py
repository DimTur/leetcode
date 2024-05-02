# https://leetcode.com/problems/move-zeroes/description/
from typing import List


def move_zeroes(nums: List[int]) -> None:
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return


nums1 = [0, 1, 0, 3, 12]
nums2 = [0]
nums3 = [0, 1]
nums4 = [0, 1, 0]

print(move_zeroes(nums1))
print(move_zeroes(nums2))
print(move_zeroes(nums3))
print(move_zeroes(nums4))
