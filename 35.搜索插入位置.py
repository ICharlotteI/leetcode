#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # target在右半边
                left = mid + 1
            elif nums[mid] > target:
                # target在左半边
                right = mid - 1
            else:
                return mid
        # left指向第一个大于target的位置  所以是要插入的位置（占据那个位置）
        # right指向最后一个小于target的位置 所以下一个才是要插入的位置
        return left


# @lc code=end
