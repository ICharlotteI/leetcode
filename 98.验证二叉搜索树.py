#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 二叉搜索树「中序遍历」得到的值构成的序列一定是升序的
        pre = float("-inf")

        def dfs(root):
            nonlocal pre
            if not root:
                return True
            # 左子树是升序的
            bool_left = dfs(root.left)
            # 当前节点大于前一个值
            bool_cur = root.val > pre
            pre = root.val
            # 右子树是升序的
            bool_right = dfs(root.right)
            return bool_left and bool_cur and bool_right

        return dfs(root)


# @lc code=end
