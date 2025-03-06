#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10e8 for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            # 跳跃一次步长
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    # 到 i+j 位置的最小跳跃次数
                    # dp[i] + 1 从i位置跳跃一次
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]


# @lc code=end
