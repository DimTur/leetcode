# https://leetcode.com/problems/search-insert-position/description/

def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left, print(left)


nums = [1, 3, 5, 6]
target = 5

search_insert(nums, target)
