#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p_len = len(p)
        sorted_p = sorted(p)
        for i in range(len(s) - p_len + 1):
            sorted_str = sorted(s[i : i + p_len])
            if sorted_str == sorted_p:
                ans.append(i)
        return ans


# @lc code=end
