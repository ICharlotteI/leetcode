#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List


class Solution:
    """
    nums 元素值互不相同
    """

    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        # nums[left]最小值   nums[right]最大值
        return nums[left]


# @lc code=end
