#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # level = 0
        # # 先找行
        # for i in range(m):
        #     if target >= matrix[i][0] and target <= matrix[i][n - 1]:
        #         level = i
        #         break
        # # 再对列做二分查找
        # left, right = 0, n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[level][mid] > target:
        #         right = mid - 1
        #     elif matrix[level][mid] < target:
        #         left = mid + 1
        #     else:
        #         return True
        # return False

        # 转换为一维
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        return False


# @lc code=end
