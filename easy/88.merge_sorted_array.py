# https://leetcode.com/problems/merge-sorted-array/description/

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums3 = []

    for i in range(m):
        nums3.append(nums1[i])
    for i in range(n):
        nums3.append(nums2[i])

    for idx, num in enumerate(sorted(nums3)):
        nums1[idx] = num


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
