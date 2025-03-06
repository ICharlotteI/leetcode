#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


# 其数字都在 [1, n] 范围内
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 代表有环 第一阶段
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 入环节点 第二阶段  重置slow 步长均一步
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# @lc code=end
