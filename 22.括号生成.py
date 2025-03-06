#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # i 目前已经有几个括号 left_count 在之中左括号数量
        def back(i, left_count):
            if i == 2 * n:
                res.append("".join(tmp))
            # 左括号还能加
            if left_count < n:
                tmp[i] = "("
                back(i + 1, left_count + 1)
            # 右括号少 还能加
            if i - left_count < left_count:
                tmp[i] = ")"
                back(i + 1, left_count)

        res = []
        tmp = [""] * (2 * n)
        back(0, 0)
        return res


# @lc code=end
