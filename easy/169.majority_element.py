# https://leetcode.com/problems/majority-element/description/

# def majority_element(nums: list[int]) -> int:
#     m_elem = nums[0]
#     max_val = 0
#     count_elements = {}
#
#     for num in nums:
#         count_elements[num] = count_elements.get(num, 0) + 1
#         if count_elements[num] > max_val:
#             max_val = count_elements[num]
#             m_elem = num
#
#     return m_elem


def majority_element(nums: list[int]) -> int:
    res = None
    count = 0

    for num in nums:
        if count == 0:
            res = num
            count += 1
        elif res == num:
            count += 1
        else:
            count -= 1

    return res


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums1))
print(majority_element(nums2))
