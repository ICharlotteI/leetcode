#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List

# 正整数数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        min_length = float('inf')
        sum_value = 0
        while r < len(nums):
            sum_value += nums[r]
            r+=1
            while sum_value >= target:
                min_length = min(min_length, r-l)
                sum_value -= nums[l]
                l+=1
        if min_length == float('inf'):
            return 0
        else:
            return min_length


# @lc code=end

