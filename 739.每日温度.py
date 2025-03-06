#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 最后一个位置没有下一天 肯定是0
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for idx, val in enumerate(temperatures):
            # 需要循环遍历栈直到栈中更大的放入栈中
            # 更高 >
            while stack and val > stack[-1][1]:
                upt_idx, upt_val = stack.pop()
                res[upt_idx] = idx - upt_idx
            stack.append((idx, val))

        return res


# @lc code=end
