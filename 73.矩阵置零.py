#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(num_rows):
            for j in range(num_cols):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0


# @lc code=end
