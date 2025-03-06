#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        sub_sum = 0

        for num in nums:
            if sub_sum > 0:
                sub_sum += num
            else:
                # 如果之前的和小于0 = 加上之前的对后面也会变得更小
                sub_sum = num

            ans = max(sub_sum, ans)
        return ans


# @lc code=end
