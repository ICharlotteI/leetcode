#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                elif i == 0 and j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
                else:
                    dp[i][j] = min(
                        dp[i][j], dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j]
                    )
        return dp[-1][-1]


# @lc code=end
