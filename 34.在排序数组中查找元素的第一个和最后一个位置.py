#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def biSearchLeft(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        # 如果有 返回的是第一个目标值位置  如果没有  返回的是应该插入的位置
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start_index = self.biSearchLeft(nums, target)
        # 说明没找到值
        if start_index >= len(nums) or nums[start_index] != target:
            return [-1, -1]

        end_index = self.biSearchLeft(nums, target + 1) - 1
        return [start_index, end_index]


# @lc code=end
