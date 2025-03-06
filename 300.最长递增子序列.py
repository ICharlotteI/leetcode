#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp[i]表示以nums[i]结尾的最长子序列长度
        n = len(nums)
        # 每个元素是一个子序列，长度为1
        dp = [1] * (n)
        for i in range(1, n):
            for j in range(i):
                # 严格递增为大于  相等不算  非严格递增为大于等于
                # 可以把nums[i]放到以前nums[j]结尾的子序列
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # 返回的不是n-1 最长递增子序列可以以中间某个值为末尾
        return max(dp)


# @lc code=end
