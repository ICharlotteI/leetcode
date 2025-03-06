#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        
        for num in num_set:
            # 先判断是否能作为起点，如果能计算以当前num作为起点的序列的长度
            if (num - 1) not in num_set:
                seq_len = 1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1
                max_len = max(max_len, seq_len)
        return max_len

# @lc code=end

