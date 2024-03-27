# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            if stack[-1].left:
                left = stack[-1].left
                stack[-1].left = None
                stack.append(left)
                continue
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
        return result

