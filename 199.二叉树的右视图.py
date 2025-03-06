#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            # 把这一层都处理  最后一个处理的就是右视图
            for i in range(size):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i == size - 1:
                    ans.append(cur_node.val)
        return ans


# @lc code=end
