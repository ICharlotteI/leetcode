#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
from typing import List


class Solution:
    """
    最小的正整数
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        # 最小的正整数肯定不会超过数组的长度+1   因为最极端的情况数组中恰好是1~n
        n = len(nums)
        # 空间复杂度超
        # for i in range(1, n + 1):
        #     if i not in nums:
        #         return i
        # return n + 1

        for i in range(n):
            # nums[i]应该放在nums[i]-1索引上
            while nums[i] >= 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# @lc code=end
