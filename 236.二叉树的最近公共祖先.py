#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root
        # 没找到p和q  继续分别往左子树和右子树找p和q
        # 从左子树找
        left = self.lowestCommonAncestor(root.left, p, q)
        # 从右子树找
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return
        
        # 左子树没有p也没有q
        # p、q都在右边  回溯的right指向右子树中的最近公共祖先
        if not left:
            return right
        # 右子树没有p也没有q
        # p、q都在左边  回溯的left指向左子树中的最近公共祖先
        if not right:
            return left
        # p和q分布在两侧 root是最近公共祖先
        return root


# @lc code=end
