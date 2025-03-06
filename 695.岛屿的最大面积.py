#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, x, y):
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] != 1:
                return 0

            grid[x][y] = 2

            return (
                1
                + dfs(grid, x - 1, y)
                + dfs(grid, x, y - 1)
                + dfs(grid, x + 1, y)
                + dfs(grid, x, y + 1)
            )

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = dfs(grid, i, j)
                    max_area = max(max_area, cur_area)
        return max_area


# @lc code=end
