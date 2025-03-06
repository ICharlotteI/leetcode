#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur_index):
            if cur_index == n:
                res.append(nums[:])
                return
            for i in range(cur_index, n):
                # 固定首位
                nums[i], nums[cur_index] = nums[cur_index], nums[i]
                # 后续数字排列  ！！cur_index指引循环范围也就是排列范围
                dfs(cur_index + 1)
                # 撤回
                nums[i], nums[cur_index] = nums[cur_index], nums[i]

        res = []
        n = len(nums)
        dfs(0)
        return res


# @lc code=end
