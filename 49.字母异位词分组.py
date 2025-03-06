#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for each in strs:
            str_index = ''.join(sorted(each))
            if str_index not in hashmap:
                hashmap[str_index] = []
            hashmap[str_index].append(each)
        for value in hashmap.values():
            ans.append(value)
        return ans

# @lc code=end

