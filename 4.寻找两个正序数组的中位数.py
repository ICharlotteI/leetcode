#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        该实现时间复杂度O(m+n)
        """
        m, n = len(nums1), len(nums2)
        total_length = m + n
        mid_index = total_length // 2

        arr1_p, arr2_p = 0, 0
        pre, cur = 0, 0
        # 在归并排序的过程中寻找中位数  需要遍历到mid_index
        for i in range(mid_index + 1):
            pre = cur
            # 优先走第一个数组
            if arr1_p < m and (arr2_p >= n or nums1[arr1_p] <= nums2[arr2_p]):
                cur = nums1[arr1_p]
                arr1_p += 1
            else:
                cur = nums2[arr2_p]
                arr2_p += 1

        if total_length % 2 == 1:
            return cur
        else:
            return (pre + cur) / 2


# @lc code=end
