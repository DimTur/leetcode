# https://leetcode.com/problems/remove-element/description/

def remove_element(nums: list[int], val: int) -> int:
    pointer = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[pointer] = nums[i]
            pointer += 1

    return pointer

nums = [0,1,2,2,3,0,4,2]
val = 2

remove_element(nums, val)