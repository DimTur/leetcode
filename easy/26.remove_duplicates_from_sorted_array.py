# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def remove_duplicates_1(nums: list[int]) -> int:
    """
    Solutin #1
    """
    nums[:] = sorted(set(nums))

    return len(nums)


# nums = [1, 1, 2]
# print(remove_duplicates_1(nums))

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates_1(nums))


def remove_duplicates_2(nums: list[int]) -> int:
    """
    Solutin #2
    """
    i = 0
    j = 1

    while j < len(nums):
        if nums[i] < nums[j]:
            i += 1
            nums[i] = nums[j]

        j += 1

    return i + 1
