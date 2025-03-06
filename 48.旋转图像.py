#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List
import copy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        tmp = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = tmp[i][j]


# @lc code=end
