#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cns_t = Counter(t)
        cns_s = Counter()
        l, r = 0, 0
        while r < len(s):
            cns_s[s[r]] += 1
            r += 1
            while cns_s >= cns_t:
                # 找到更短的子串
                if r - l < ans_right - ans_left:
                    ans_left, ans_right = l, r
                cns_s[s[l]] -= 1
                l += 1
        # 否则返回涵盖的最小子串(不是长度,长度应该是ans_right-ans_left)
        return "" if ans_left < 0 else s[ans_left:ans_right]


# @lc code=end
