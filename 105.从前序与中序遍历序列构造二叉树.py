#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List, Optional
from collections import defaultdict


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def recur(pre_root_index, in_left, in_right):
            # 不能有=  否则会将叶子节点跳过
            if in_left > in_right:
                return None
            in_root_index = dic[preorder[pre_root_index]]
            # 左子树的根节点
            left_node = recur(
                pre_root_index + 1, in_left, in_root_index - 1
            )
            # 右子树的根节点
            right_node = recur(
                # 根节点索引 + 左子树长度 + 1
                pre_root_index + in_root_index - in_left + 1,
                in_root_index + 1,
                in_right,
            )
            root_node = TreeNode(preorder[pre_root_index], left_node, right_node)
            # 返回根节点
            return root_node

        dic = defaultdict(int)
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        root = recur(0, 0, len(inorder) - 1)
        return root


# @lc code=end
