#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            # 两种选择 当前的不偷dp[i - 1]   当前的偷dp[i - 2] + nums[i]
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i-1])
        return dp[n]


# @lc code=end
