#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # 先设置为都是1的最多情况
            dp[i] = i
            j = 1
            while i - j * j >= 0:
                # 和为i - j*j的完全平方数的最小数量
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


# @lc code=end
