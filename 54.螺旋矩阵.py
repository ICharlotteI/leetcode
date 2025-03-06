#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        l, t, r, b = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        while True:
            # left to right
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            if t > b:
                break
            # top to bottom
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                ans.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return ans


# @lc code=end
