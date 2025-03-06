#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j =0, len(height) - 1
        ans = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > ans:
                ans = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
# @lc code=end

