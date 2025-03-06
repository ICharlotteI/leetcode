#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []

        good_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    good_count += 1

        die_time = 0
        # 如果初始有多个烂橘子  同时广度扩散感染
        # 如果好橘子都已经被腐烂了  那就已经结束了
        while queue and good_count > 0:
            die_time += 1
            num_nodes = len(queue)
            for i in range(num_nodes):
                x, y = queue.pop(0)
                if 0 <= x - 1 < m and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    good_count -= 1
                    queue.append((x - 1, y))
                if 0 <= y - 1 < n and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    good_count -= 1
                    queue.append((x, y - 1))
                if 0 <= x + 1 < m and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    good_count -= 1
                    queue.append((x + 1, y))
                if 0 <= y + 1 < n and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    good_count -= 1
                    queue.append((x, y + 1))

        if good_count > 0:
            return -1
        else:
            return die_time


# @lc code=end
