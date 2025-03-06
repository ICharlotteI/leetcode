#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # 翻转左子树，翻回翻转后的根节点
        left = self.invertTree(root.left)
        # 翻转右子树，翻回翻转后的根节点
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


# @lc code=end
