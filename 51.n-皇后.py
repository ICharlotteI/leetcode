#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(row):
            if row == n:
                res.append(
                    [
                        "." * queen_col + "Q" + "." * (n - 1 - queen_col)
                        for queen_col in queens
                    ]
                )
                return

            for col, isHave in enumerate(cols):
                # 判断这列能否放皇后
                if not isHave and not diag1[row + col] and not diag2[row - col]:
                    queens[row] = col  # 直接覆盖不用恢复
                    cols[col] = True
                    diag1[row + col] = True
                    diag2[row - col] = True
                    # 下一行上找合适的位置放皇后
                    dfs(row + 1)
                    # 恢复
                    cols[col] = False
                    diag1[row + col] = False
                    diag2[row - col] = False

        res = []
        # 第index行的皇后在第几列
        queens = [0] * n
        # 列上是否有皇后
        cols = [False] * n
        # 主对角线 False攻击不到 最大索引是（n-1+n-1）
        diag1 = [False] * (2 * n - 1)
        # 副对角线 False攻击不到
        diag2 = [False] * (2 * n - 1)
        # 从第0行开始找结果
        dfs(0)
        return res


# @lc code=end
