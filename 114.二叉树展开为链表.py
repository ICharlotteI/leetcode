#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 后序遍历
        def dfs(root):
            if not root:
                return
            pre = None
            dfs(root.left)
            dfs(root.right)
            if root.left:
                pre = root.left
                # 找到左子树的最右节点
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None

        dfs(root)


# @lc code=end
