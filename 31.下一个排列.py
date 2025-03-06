#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        i, j = n - 2, n - 1
        # 找尽可能靠右侧的小数，从右往左第一个升序的左边元素就是要交换的小数
        # 必须升序  要不可能是降序中相同的数
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        # i<0时j=0 是最后一个排列
        if i >= 0:
            k = n - 1
            # [j,n-1]倒序的  找尽可能小的大数 第一个nums[k]大于nums[i]
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
            
        i, j = j, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# @lc code=end
