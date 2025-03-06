#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, x, y):
            # '0'水 '2'已经遍历过的陆地
            if (
                not 0 <= x < m
                or not 0 <= y < n
                or grid[x][y] == "0"
                or grid[x][y] == "2"
            ):
                return
            grid[x][y] = "2"
            dfs(grid, x - 1, y)
            dfs(grid, x, y - 1)
            dfs(grid, x + 1, y)
            dfs(grid, x, y + 1)

        # 遇到一个1开始dfs表示有一片陆地
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 主要目的是将该片陆地遍历变为2
                    dfs(grid, i, j)
                    count += 1
        return count


# @lc code=end
