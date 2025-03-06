#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # step 第几步
        def dfs(x, y, step):
            if (
                not 0 <= x < m
                or not 0 <= y < n
                or visited[x][y] == 1
                or not 0 <= step < str_len
                or word[step] != board[x][y]
            ):
                return False
            if step == str_len - 1:
                return True
            visited[x][y] = 1
            res = (
                dfs(x + 1, y, step + 1)
                or dfs(x, y + 1, step + 1)
                or dfs(x - 1, y, step + 1)
                or dfs(x, y - 1, step + 1)
            )
            # 回溯成为未访问状态  要不会影响其他节点遍历时的结果
            visited[x][y] = 0
            return res

        m, n = len(board), len(board[0])
        str_len = len(word)
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end
