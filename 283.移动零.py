#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j =0, 0
        while j < len(nums):
            if nums[j] != 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                i += 1
            j += 1

"""
[1,0,0,3,12]
[1,3,0,0,12]
[1,3,12,0,0]
"""
# @lc code=end

