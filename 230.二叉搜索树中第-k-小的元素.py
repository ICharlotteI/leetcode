#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # n>=1
        ans = 0
        counter = 0

        def dfs(root):
            nonlocal counter, ans
            if not root:
                return
            dfs(root.left)
            counter += 1
            if counter == k:
                ans = root.val
            dfs(root.right)

        dfs(root)

        return ans


# @lc code=end
