#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if s == "":
            return ans

        # i, j = 0, 0
        # # temp存储不含有重复字符的子串
        # temp = []
        # while i < len(s) and j < len(s):
        #     if s[j] in temp:
        #         temp = []
        #         i += 1
        #         j = i
        #     else:
        #         temp.append(s[j])
        #         j += 1
        #         ans = max(ans, len(temp))

        # 改进——找到一个符合的子串那么之后的长度至少不能再短了
        i, j = 0, 0
        # temp存储不含有重复字符的子串
        temp = ""
        while i < len(s) and j < len(s):
            if len(set(temp)) != len(temp):
                i += 1
                j += 1
                temp = s[i:j]
                continue
            if s[j] in temp:
                i += 1
                j += 1
                temp = s[i:j]
            else:
                temp += s[j]
                j += 1
                ans = max(ans, len(temp))

        return ans


# @lc code=end
