#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        # 索引大小即是到当前位置需要几步
        for index, num in enumerate(nums):
            # 前面能走的最远距离到不了当前索引  也就没法继续往后走
            if index > max_len:
                return False
            # 更新包含当前能走的最远距离
            max_len = max(max_len, index + num)
        return True


# @lc code=end
