# https://leetcode.com/problems/single-number/description/
from typing import List


def single_number(nums: List[int]) -> int:
    count_nums = {}

    for num in nums:
        if num in count_nums:
            count_nums[num] += 1
        else:
            count_nums[num] = 1

    for num, s in count_nums.items():
        if s == 1:
            return num


nums = [4, 1, 2, 1, 2]

print(single_number(nums))
