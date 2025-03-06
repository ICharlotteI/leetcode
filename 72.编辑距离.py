#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, n + 1):
            # word1没有字符时 word2字符多长就是要操作的步数  因为是插入
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, m + 1):
            # word2没有字符时 word1字符多长就是要操作的步数  因为是删除
            dp[i][0] = dp[i - 1][0] + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 第i个字符的索引是i-1
                if word1[i - 1] == word2[j - 1]:
                    # 不需要操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i][j-1] 插入
                    # dp[i-1][j] 删除
                    # dp[i-1][j-1] 最少的操作是替换
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[m][n]


# @lc code=end
