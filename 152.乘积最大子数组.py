#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 由于负数 当前位置的最优解未必是由前一个位置的最优解转移得到的
        # max_dp 以第i个元素结尾的乘积最大子数组的乘积
        # min_dp 以第i个元素结尾的乘积最小子数组的乘积
        max_dp, min_dp = nums.copy(), nums.copy()
        n = len(nums)
        for i in range(1, n):
            #  nums[i]可能正数可能负数  负数的话希望前面的积是尽可能小的负数->min_dp[i-1]
            max_dp[i] = max(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
        # 题目要乘积“最大”“子”数组的乘积  并不一定以n-1结尾 而最大的从max里找
        return max(max_dp)


# @lc code=end
