# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while head:
            if not head.next or head.val != head.next.val:
                tail.next = head
                tail = tail.next

            head = head.next

        tail.next = None

        return dummy.next

# def delete_duplicates(head: list[int]) -> list[int]:
#     new_array = set(head)
#     result = [x for x in new_array]
#     print(result)
#
#
# head_1 = [1, 1, 2]
# head_2 = [1, 1, 2, 3, 3]
#
# delete_duplicates(head_1)
# delete_duplicates(head_2)

