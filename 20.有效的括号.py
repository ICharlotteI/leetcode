#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
            elif not stack:
                return False
            elif ch == ")":
                pop_ch = stack.pop()
                if pop_ch != "(":
                    return False
            elif ch == "]":
                pop_ch = stack.pop()
                if pop_ch != "[":
                    return False
            elif ch == "}":
                pop_ch = stack.pop()
                if pop_ch != "{":
                    return False
        return not stack


# @lc code=end
