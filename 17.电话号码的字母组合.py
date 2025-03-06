#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List

phoneMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [char for char in phoneMap.get(digits[0])]
        for i in range(1, len(digits)):
            cur_char_list = [char for char in phoneMap.get(digits[i])]
            temp = []
            for each in res:
                for ch in cur_char_list:
                    temp.append(each + ch)
            res = temp
        return res


# @lc code=end
