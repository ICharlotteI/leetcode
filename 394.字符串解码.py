#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        multiple = 0
        for char in s:
            if char is "[":
                # 括号中的字符串有几倍   前面的需要拼接的字符串
                stack.append((multiple, res))
                multiple = 0
                res = ""
            elif char is "]":
                cur_multiple, last_res = stack.pop()
                # 此时的res是括号内的子串
                res = last_res + cur_multiple * res
            elif "0" <= char <= "9":
                multiple = multiple * 10 + int(char)
            else:
                res += char

        return res


# @lc code=end
