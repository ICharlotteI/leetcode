#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 穷举所有的可能  检测以node为起始节点且向下延深的路径有多少种
        def dfs(root, targetSum) -> int:
            if not root:
                return 0

            ans = 0
            # 恰好当前节点就是一条路径
            if root.val == targetSum:
                ans += 1

            ans += dfs(root.left, targetSum - root.val)
            ans += dfs(root.right, targetSum - root.val)
            return ans

        if not root:
            return 0
        ans = dfs(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans


# @lc code=end
