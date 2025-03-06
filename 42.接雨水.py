#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        # 按行求
        # max_height = max(height)
        # for level in range(max_height):
        #     is_start = False
        #     temp = 0
        #     for each in height:
        #         if each >= (level+1):
        #             is_start = True
        #             ans += temp
        #             temp = 0
        #         elif is_start:
        #             temp += 1

        # 按列求  最两端的列一定没水
        # for index, cur_height in enumerate(height):
        #     if index == 0 or index == len(height)-1:
        #         continue
        #     max_left = max(height[:index])
        #     max_right = max(height[index+1:])
        #     l_r_min = min(max_left, max_right)
        #     if cur_height >= l_r_min:
        #         # 无法储水
        #         continue
        #     else:
        #         ans += (l_r_min-cur_height)

        # 双指针
        l, r = 0, len(height) - 1
        max_left, max_right = 0, 0
        while l < r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            # 找较矮的   较矮的-当前列=当前列储水
            if max_left < max_right:
                # l列可以储水，计算l列的储水量
                ans += max_left - height[l]
                # 从左向右走
                l += 1
            else:
                # r列可以储水，计算r列的储水量
                ans += max_right - height[r]
                # 从右向左走
                r -= 1
            # 直到所有列算完
        return ans


# @lc code=end
