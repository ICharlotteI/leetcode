#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 最大路径和
        maxSum = float("-inf")

        def maxGain(root):
            nonlocal maxSum
            if not root:
                return 0

            # 舍弃负值  负值贡献的节点放到路径里一定会产生副作用  贡献设置为0以表示不参与路径
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)

            maxSum = max(maxSum, leftGain + rightGain + root.val)

            # 返回当前节点的贡献  用于给上层节点构建最大路径  只会走一边  选最大的一边就好
            return root.val + max(leftGain, rightGain)

        maxGain(root)

        return maxSum


# @lc code=end
