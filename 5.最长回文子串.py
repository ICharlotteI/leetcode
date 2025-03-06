#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        # (i,j) 表示字符串 s 的第i到j个字母组成的串是否是回文串
        dp = [[False] * length for _ in range(length)]

        for i in range(length):
            # 每个字符构成的串（子串长度为1）
            dp[i][i] = True
        max_len = 1
        begin = 0
        # 先枚举子串长度
        for L in range(2, length + 1):
            # 枚举起点索引
            for i in range(length):
                # 终点索引
                j = i + L - 1

                # j超了直接跳出循环
                if j >= length:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if L <= 3:
                        dp[i][j] = True
                    else:
                        # 并不会越界 不是[i+1:j-1] dp是n*n矩阵 当i+1>j-1时默认值就是False
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and L > max_len:
                    max_len = L
                    begin = i

        # 最长回文子串
        return s[begin : begin + max_len]


# @lc code=end
