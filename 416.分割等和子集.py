#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        # 两个子集的元素和相等 = 两个子集的元素和都为总和的一半
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            # 不是2的倍数肯定分不了两个和一样的子集
            return False

        target = nums_sum // 2
        if max(nums) > target:
            # 最大值比和的一半都大了  那剩下的子集的和肯定小于和的一半  也就没法分成两个和一样的子集
            return False

        # dp[i][j]表示从数组的[0,i]下标范围内选取若干个正整数（可以不选），是否存在一种选取方案使得被选取的正整数的和等于j（可以是0）
        dp = [[False] * (target + 1) for _ in range(n)]
        # 让和（j）等于0肯定有选取方案，就是不选，所以是True
        for i in range(n):
            dp[i][0] = True

        # 对于i=0时子数组[0:0]只有一种选取就是j=nums[0]会是true 没有和别的加的机会
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if num > j:
                    # 不能选num
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可以选取num也可以不选取
                    dp[i][j] = dp[i - 1][j - num] | dp[i - 1][j]

        return dp[n - 1][target]


# @lc code=end
