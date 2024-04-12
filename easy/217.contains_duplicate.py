# https://leetcode.com/problems/contains-duplicate/description/

def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]

print(contains_duplicate(nums1))
print(contains_duplicate(nums2))
