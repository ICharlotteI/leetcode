#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 分割出来的子串在原串中是连续的
        def back(i):
            if i >= str_len:
                res.append(tmp_strs.copy())
                return
            # 遍历字串结束的位置  i为字符串起点 j为终点
            for j in range(i, str_len):
                # 不包含j+1位置
                cur_str = s[i : j + 1]
                # 判断是否回文
                if cur_str == cur_str[::-1]:
                    tmp_strs.append(cur_str)
                    # 考虑前面子串是否回文  回文则添加  然后将其与该子串后面部分分割出来的回文串结合   s[i : j + 1]与j+1往后
                    back(j + 1)
                    tmp_strs.pop()

        res = []
        tmp_strs = []
        str_len = len(s)
        back(0)
        return res


# @lc code=end
