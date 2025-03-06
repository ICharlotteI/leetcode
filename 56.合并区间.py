#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        i = 0
        while i < len(intervals):
            left, right = intervals[i]
            # 倒数第二个
            while i < len(intervals) - 1 and intervals[i + 1][0] <= right:
                right = max(intervals[i + 1][1], right)
                i += 1
            ans.append([left, right])
            i += 1
        return ans


# @lc code=end
