#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List


# 找字符最后出现的位置 该字符在一个子串里
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 记录每个字符最后出现的位置
        last_dic = {ch: i for i, ch in enumerate(s)}

        res = []
        tmp_len = 0
        max_pos = last_dic[s[0]]  # 第一个字符最后出现的位置
        for i, ch in enumerate(s):
            tmp_len += 1
            if last_dic[ch] > max_pos:
                max_pos = last_dic[ch]
            # 到了某些字符最后出现的位置 表示可以截断了
            if i == max_pos:
                res.append(tmp_len)
                tmp_len = 0
        return res


# @lc code=end
