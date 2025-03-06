#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 只要某次选择的基准为倒数第k个下标就是结果（右边都大，左边都小）   不用关心前后是否已排序好
        def quickSelect(arr, k):
            pivot = random.choice(arr)
            left, right, equal = [], [], []
            for val in arr:
                if val < pivot:
                    left.append(val)
                elif val > pivot:
                    right.append(val)
                else:
                    equal.append(val)
            # 说明倒数第K大在right中
            if k <= len(right):
                return quickSelect(right, k)
            # 说明倒数第K大在left中
            elif len(arr) - k < len(left):
                # 应该在left中排倒数第几大   k - (len(right) + len(equal))
                # 和pivot相等的值在数组中未必只有一个
                return quickSelect(left, k - (len(right) + len(equal)))
            else:
                return pivot

        return quickSelect(nums, k)


# @lc code=end
