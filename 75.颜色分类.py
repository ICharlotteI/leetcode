#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                # 下一个要交换成0的位置
                p0 += 1
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                # 下一个要交换成2的位置
                p2 -= 1
                # 交换后的num[i]仍然可能是0或2，会被忽略处理，需要回退再处理一遍
                if nums[i] == 0 or nums[i] == 2:
                    i -= 1
            i += 1


# @lc code=end
