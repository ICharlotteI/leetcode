#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans

        # 每个结点的直径都要被保存，比较以当前节点为根时的直径
        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            # 以当前节点为根时的直径
            diameter = l + r
            nonlocal ans
            ans = max(ans, diameter)
            return max(l, r) + 1

        depth(root)
        return ans


# @lc code=end
