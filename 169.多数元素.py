#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dic = defaultdict(int)
        # for num in nums:
        #     dic[num] += 1

        # for index, value in dic.items():
        #     if value > len(nums) //2:
        #         return index

        # return 0

        candidate = nums[0]
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num

            if candidate == num:
                counter += 1
            else:
                counter -= 1

        return candidate


# @lc code=end
