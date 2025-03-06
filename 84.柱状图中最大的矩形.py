#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List


class Solution:
    # heights 非负整数
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 当前高度对应的最大面积的宽度 右边比他小的第一个 - 左边比它小的第一个 - 1
        # 才能以当前高度为长构建矩形
        res = 0
        stack = []
        # 增加第一个的左边界 最后一个的右边界
        heights.insert(0, 0)
        heights.append(0)
        for index, height in enumerate(heights):
            # 单调增栈   要弹出  那么新元素是栈顶元素的下一个小的
            while stack and heights[stack[-1]] > height:
                # 待计算当前高度面积的——栈顶元素
                cur_index = stack.pop()
                # 能直接用-1索引是因为在heights开头加了0元素，且非负整数能保证栈中至少有一个0
                # 右边第一个小的
                right = index
                # 左边第一个小的
                left = stack[-1]
                res = max(res, (right - left - 1) * heights[cur_index])
            stack.append(index)
        return res


# @lc code=end
