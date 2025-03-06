#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(target, index):
            # 终止条件
            if target < 0:
                return
            if target == 0:
                # 深拷贝一个结果
                res.append(tmp_combine.copy())
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    tmp_combine.append(candidates[i])
                    back(target - candidates[i], i)
                    tmp_combine.pop()

        res = []
        tmp_combine = []
        # 排序，后面的元素更大，更容易得到所有小的选择
        candidates.sort()
        back(target, 0)
        return res


# @lc code=end
