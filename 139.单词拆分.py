#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # 前i位可以用wordDict中的表示
        dp = [False] * (n + 1)
        dp[0] = True
        # 起点  要从头开始
        for i in range(n):
            # 终点
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[n]

# @lc code=end
